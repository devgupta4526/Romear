from collections.abc import Iterator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError
from sqlalchemy.exc import OperationalError

from app.config import Settings
from app.main import create_app
from app.schemas import PageQuery


@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(create_app(Settings(_env_file=None))) as test_client:
        yield test_client


def test_health_and_version(client: TestClient) -> None:
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/v1").json() == {"service": "romear-api", "api_version": "v1", "stage": "00"}


def test_startup_is_not_fabricated() -> None:
    with TestClient(create_app(Settings(_env_file=None))) as test_client:
        test_client.app.state.started = False
        assert test_client.get("/health").status_code == 503
        assert test_client.get("/ready").status_code == 503


def test_readiness_checks_database_and_schema(client: TestClient) -> None:
    factory = MagicMock()
    session = factory.return_value.__enter__.return_value
    session.execute.return_value.scalar.return_value = "0001_infrastructure"
    client.app.state.session_factory = factory
    assert client.get("/ready").json() == {"status": "ready"}
    session.execute.return_value.scalar.return_value = "stale"
    stale = client.get("/ready")
    assert stale.status_code == 503
    assert stale.json()["error"]["code"] == "schema_not_ready"
    factory.side_effect = OperationalError("sensitive_sql", {}, Exception("secret"))
    failure = client.get("/ready")
    assert failure.status_code == 503
    assert "secret" not in failure.text
    assert "sensitive_sql" not in failure.text


def test_unknown_route_and_mutation_denied(client: TestClient) -> None:
    for response in (client.get("/v1/users"), client.post("/v1")):
        assert response.status_code in {404, 405}
        assert response.json()["error"]["request_id"] == response.headers["X-Request-ID"]
        assert response.headers["Cache-Control"] == "no-store"


def test_repeated_checks_are_stateless(client: TestClient) -> None:
    first, second = client.get("/health"), client.get("/health")
    assert first.json() == second.json()
    assert first.headers["X-Request-ID"] != second.headers["X-Request-ID"]


def test_unhandled_failure_is_redacted() -> None:
    application = create_app(Settings(_env_file=None))

    @application.get("/test-only-failure", include_in_schema=False)
    def fail() -> None:
        raise RuntimeError("private-internal-value")

    with TestClient(application) as client:
        response = client.get("/test-only-failure")
    assert response.status_code == 500
    assert response.json()["error"]["code"] == "internal_error"
    assert "private-internal-value" not in response.text


def test_openapi_contract(client: TestClient) -> None:
    schema = client.get("/v1/openapi.json").json()
    assert set(schema["paths"]) == {"/health", "/ready", "/v1"}
    assert "503" in schema["paths"]["/ready"]["get"]["responses"]
    assert "ErrorEnvelope" in schema["components"]["schemas"]


def test_cors_denies_unknown_origin(client: TestClient) -> None:
    response = client.options(
        "/v1",
        headers={"Origin": "https://untrusted.example", "Access-Control-Request-Method": "GET"},
    )
    assert response.status_code == 400
    assert "access-control-allow-origin" not in response.headers


@pytest.mark.parametrize("env", ["staging", "prod"])
def test_nondev_rejects_test_data_and_unsafe_config(env: str) -> None:
    with pytest.raises(ValidationError):
        Settings(_env_file=None, env=env, allow_test_data=True)
    with pytest.raises(ValidationError):
        Settings(_env_file=None, env=env)
    safe = Settings(
        _env_file=None,
        env=env,
        database_url="postgresql+psycopg://user:configured@db/romear?sslmode=require",
        cors_origins=["https://dashboard.example.com"],
    )
    assert not safe.allow_test_data


def test_pagination_bounds_and_club_threshold() -> None:
    assert PageQuery().limit == 20
    for limit in (0, 101):
        with pytest.raises(ValidationError):
            PageQuery(limit=limit)
    with pytest.raises(ValidationError):
        Settings(_env_file=None, club_min_verified_members=3)


def test_invalid_configuration_does_not_expose_credentials() -> None:
    with pytest.raises(ValidationError) as failure:
        Settings(
            _env_file=None,
            env="prod",
            database_url="postgresql+psycopg://user:private-credential@db/romear",
        )
    assert "private-credential" not in str(failure.value)
