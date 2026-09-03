from __future__ import annotations

from typing import Any, Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaginatedList(SdkBaseModel):
    """A paginated list of results returned by list and query endpoints. All paginated responses follow the same
    structure with a results array, pagination info, and object type."""

    object_: Literal["list"] = Field(default="list", alias="object")
    """Always "list" for paginated responses."""

    results: list[Any]
    """The array of result objects for the current page."""

    next_cursor: str | None
    """The cursor to use for the next page of results, or null if there are no more results."""

    has_more: bool
    """Whether there are more results available beyond this page."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of objects in the results array."""

    request_id: Optional[str] = UNSET
    """A unique identifier for this API request."""


class PaginatedListDict(TypedDict):
    object_: NotRequired[Literal["list"]]
    results: list[Any]
    next_cursor: str | None
    has_more: bool
    type_: NotRequired[str]
    request_id: NotRequired[str]
