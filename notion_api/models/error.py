from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.object3 import Object3OrStr


class Error(SdkBaseModel):
    """An error response from the Notion API."""

    object_: Object3OrStr = Field(alias="object")
    """Always "error" for error responses."""

    status: int
    """The HTTP status code."""

    code: str
    """A machine-readable error code. Common codes include invalid_json, invalid_request_url, invalid_request,
    validation_error, missing_version, unauthorized, restricted_resource, object_not_found, conflict_error,
    rate_limited, internal_server_error, service_unavailable, and database_connection_unavailable."""

    message: str
    """A human-readable error message."""

    request_id: Optional[str] = UNSET
    """A unique identifier for the failed request."""


class ErrorDict(TypedDict):
    object_: Object3OrStr
    status: int
    code: str
    message: str
    request_id: NotRequired[str]
