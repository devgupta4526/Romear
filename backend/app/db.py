from collections.abc import Iterator
from datetime import datetime

from sqlalchemy import DateTime, Engine, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

from app.config import Settings


class Base(DeclarativeBase):
    pass


class InfrastructureMetadata(Base):
    """An empty infrastructure table; no social/domain records or seed data."""

    __tablename__ = "infrastructure_metadata"
    key: Mapped[str] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


def build_engine(settings: Settings) -> Engine:
    return create_engine(
        settings.database_url,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=5,
        pool_timeout=3,
        connect_args={"connect_timeout": 3, "options": "-c timezone=UTC -c statement_timeout=3000"},
        hide_parameters=True,
    )


def session_scope(factory: sessionmaker[Session]) -> Iterator[Session]:
    # No implicit commit: later mutations must explicitly choose a transaction boundary.
    with factory() as session:
        yield session
