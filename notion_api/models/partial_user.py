from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.object2 import Object2OrStr


class PartialUser(SdkBaseModel):
    """A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields."""

    object_: Object2OrStr = Field(alias="object")
    """Always "user"."""

    id: UUID
    """Unique identifier for the user."""


class PartialUserDict(TypedDict):
    object_: Object2OrStr
    id: UUID
