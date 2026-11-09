import json
import logging
import time
from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from starlette.exceptions import HTTPException

from app.config import Settings
from app.db import build_engine
from app.schemas import ApiError, ErrorEnvelope, Health, Ready, VersionInfo

SCHEMA_REVISION = "0001_infrastructure"
logger = logging.getLogger("romear")
logger.setLevel(logging.INFO)
if not logger.handlers:
    logger.addHandler(logging.StreamHandler())
logger.propagate = False


def error_response(request: Request, status: int, code: str, message: str) -> JSONResponse:
    body = ErrorEnvelope(
        error=ApiError(code=code, message=message, request_id=request.state.request_id)
    )
    return JSONResponse(status_code=status, content=body.model_dump())


def create_app(settings: Settings | None = None) -> FastAPI:
    config = settings or Settings()
    engine = build_engine(config)

    @asynccontextmanager
    async def lifespan(application: FastAPI) -> AsyncIterator[None]:
        application.state.started = True
        try:
            yield
        finally:
            application.state.started = False
            engine.dispose()

    application = FastAPI(
        title="ROMEAR API",
        version="0.0.1",
        openapi_url="/v1/openapi.json",
        docs_url="/v1/docs" if config.env != "prod" else None,
        redoc_url=None,
        lifespan=lifespan,
        responses={422: {"model": ErrorEnvelope}, 500: {"model": ErrorEnvelope}},
    )
    application.state.started = False
    application.state.session_factory = sessionmaker(engine, expire_on_commit=False)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=config.cors_origins,
        allow_methods=["GET"],
        allow_headers=["Accept"],
        allow_credentials=False,
    )

    @application.middleware("http")
    async def request_context(
        request: Request, call_next: Callable[[Request], Awaitable[JSONResponse]]
    ) -> JSONResponse:
        request.state.request_id = str(uuid4())
        start = time.monotonic()
        try:
            response = await call_next(request)
        except Exception:
            # Do not log exceptions/URLs/headers that could contain credentials or PII.
            response = error_response(request, 500, "internal_error", "An internal error occurred")
        response.headers["X-Request-ID"] = request.state.request_id
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        logger.info(
            json.dumps(
                {
                    "event": "http_request",
                    "request_id": request.state.request_id,
                    "method": request.method,
                    "status": response.status_code,
                    "duration_ms": round((time.monotonic() - start) * 1000),
                }
            )
        )
        return response

    @application.exception_handler(HTTPException)
    async def http_error(request: Request, exc: HTTPException) -> JSONResponse:
        return error_response(request, exc.status_code, "http_error", "Request not available")

    @application.exception_handler(RequestValidationError)
    async def validation_error(request: Request, exc: RequestValidationError) -> JSONResponse:
        return error_response(request, 422, "validation_error", "Request validation failed")

    @application.get(
        "/health",
        response_model=Health,
        tags=["Infrastructure"],
        responses={503: {"model": ErrorEnvelope}},
    )
    def health(request: Request) -> Health | JSONResponse:
        if not request.app.state.started:
            return error_response(request, 503, "not_started", "Service has not started")
        return Health()

    @application.get(
        "/ready",
        response_model=Ready,
        tags=["Infrastructure"],
        responses={503: {"model": ErrorEnvelope}},
    )
    def ready(request: Request) -> Ready | JSONResponse:
        if not request.app.state.started:
            return error_response(request, 503, "not_started", "Service has not started")
        try:
            with request.app.state.session_factory() as session:
                session.execute(text("SELECT 1"))
                revision = session.execute(text("SELECT version_num FROM alembic_version")).scalar()
                if revision != SCHEMA_REVISION:
                    return error_response(
                        request, 503, "schema_not_ready", "Database migration required"
                    )
        except SQLAlchemyError:
            return error_response(request, 503, "database_unavailable", "Database is not ready")
        return Ready()

    @application.get("/v1", response_model=VersionInfo, tags=["Infrastructure"])
    def version() -> VersionInfo:
        return VersionInfo()

    return application
