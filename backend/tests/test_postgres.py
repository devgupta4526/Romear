import os
from contextlib import contextmanager
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import inspect, text
from sqlalchemy.orm import sessionmaker

from app.config import Settings
from app.db import build_engine, session_scope
from app.main import create_app


@pytest.mark.integration
def test_clean_postgres_migration_roundtrip(monkeypatch: pytest.MonkeyPatch) -> None:
    url = os.getenv("ROMEAR_TEST_DATABASE_URL")
    if not url:
        pytest.skip("Set ROMEAR_TEST_DATABASE_URL to an EMPTY disposable PostgreSQL test database")
    # Never operate on the application DB: explicit test DB name is mandatory.
    settings = Settings(_env_file=None, database_url=url)
    engine = build_engine(settings)
    assert (engine.url.database or "").endswith("_test"), "Disposable DB must end in _test"
    assert not inspect(engine).get_table_names(), "Integration test requires a blank database"
    monkeypatch.setenv("ROMEAR_DATABASE_URL", url)
    config = Config("alembic.ini")
    command.upgrade(config, "head")
    command.upgrade(config, "head")  # Repeat is idempotent.
    command.check(config)  # SQLAlchemy metadata and migration agree.
    assert set(inspect(engine).get_table_names()) == {"alembic_version", "infrastructure_metadata"}
    with TestClient(create_app(settings)) as client:
        assert client.get("/ready").status_code == 200
    with engine.connect() as conn:
        assert conn.execute(text("SHOW timezone")).scalar() == "UTC"
        assert conn.execute(text("SELECT count(*) FROM infrastructure_metadata")).scalar() == 0
    factory = sessionmaker(engine)
    with session_scope_for_test(factory) as session:
        session.execute(text("INSERT INTO infrastructure_metadata (key) VALUES ('rollback-test')"))
    with factory() as session:
        assert session.execute(text("SELECT count(*) FROM infrastructure_metadata")).scalar() == 0
    command.downgrade(config, "base")
    assert "infrastructure_metadata" not in inspect(engine).get_table_names()
    command.upgrade(config, "head")
    engine.dispose()
    # This schema is exported by a separate deterministic command after checks.
    assert Path("migrations/versions/0001_infrastructure.py").is_file()


session_scope_for_test = contextmanager(session_scope)
