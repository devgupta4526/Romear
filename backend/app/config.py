from typing import Literal

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import make_url


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="ROMEAR_", env_file="../.env", extra="ignore", hide_input_in_errors=True
    )

    env: Literal["dev", "staging", "prod"] = "dev"
    database_url: str = "postgresql+psycopg://localhost/romear"
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:5173"])
    allow_test_data: bool = False
    club_min_verified_members: int = Field(default=4, ge=4)

    @model_validator(mode="after")
    def guard_environment(self) -> Settings:
        url = make_url(self.database_url)
        if url.drivername != "postgresql+psycopg":
            raise ValueError("PostgreSQL with psycopg is required")
        if self.env != "dev":
            if self.allow_test_data:
                raise ValueError("Test data is forbidden outside dev")
            if not url.password or url.password == "local_development_only":
                raise ValueError("Configure a non-development database credential")
            if url.query.get("sslmode") not in {"require", "verify-ca", "verify-full"}:
                raise ValueError("Database TLS is required outside dev")
            if any(not origin.startswith("https://") for origin in self.cors_origins):
                raise ValueError("CORS origins must use HTTPS outside dev")
        if "*" in self.cors_origins:
            raise ValueError("Wildcard CORS is forbidden")
        return self
