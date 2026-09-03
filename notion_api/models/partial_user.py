from __future__ import annotations

from typing import Literal
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class PartialUser(SdkBaseModel):
    """A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields."""

    object_: Literal["user"] = Field(default="user", alias="object")
    """Always "user"."""

    id: UUID
    """Unique identifier for the user."""


class PartialUserDict(TypedDict):
    object_: NotRequired[Literal["user"]]
    id: UUID
