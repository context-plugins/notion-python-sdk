from __future__ import annotations

from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr


class Parent(SdkBaseModel):
    """A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page,
    database, or block."""

    type_: TypeOrStr = Field(alias="type")
    """The type of parent."""

    database_id: Optional[UUID] = UNSET
    """The ID of the parent database. Present when type is "database_id"."""

    page_id: Optional[UUID] = UNSET
    """The ID of the parent page. Present when type is "page_id"."""

    block_id: Optional[UUID] = UNSET
    """The ID of the parent block. Present when type is "block_id"."""

    workspace: Optional[bool] = UNSET
    """Always true when the parent is the workspace. Present when type is "workspace"."""


class ParentDict(TypedDict):
    type_: TypeOrStr
    database_id: NotRequired[UUID]
    page_id: NotRequired[UUID]
    block_id: NotRequired[UUID]
    workspace: NotRequired[bool]
