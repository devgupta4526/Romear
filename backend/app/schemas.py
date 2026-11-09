from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Health(BaseModel):
    status: Literal["ok"] = "ok"


class Ready(BaseModel):
    status: Literal["ready"] = "ready"


class VersionInfo(BaseModel):
    service: str = "romear-api"
    api_version: str = "v1"
    stage: str = "00"


class ApiError(BaseModel):
    code: str
    message: str
    request_id: str


class ErrorEnvelope(BaseModel):
    error: ApiError


class Page[T](BaseModel):
    model_config = ConfigDict(extra="forbid")
    items: list[T]
    next_cursor: str | None = None
    has_more: bool = False


class PageQuery(BaseModel):
    model_config = ConfigDict(extra="forbid")
    limit: int = Field(default=20, ge=1, le=100)
    cursor: str | None = Field(default=None, max_length=512)
