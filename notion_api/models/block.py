from __future__ import annotations

from typing import Literal
from uuid import UUID

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.type1 import Type1OrStr
from .parent import Parent, ParentDict
from .partial_user import PartialUser, PartialUserDict


class Block(SdkBaseModel):
    """A Block object represents a piece of content within a Notion page. Blocks are the building blocks of all page
    content and can be of many types including paragraphs, headings, lists, images, code, tables, and more. Blocks can
    contain other blocks as children, forming a tree structure."""

    object_: Literal["block"] = Field(default="block", alias="object")
    """Always "block" for block objects."""

    id: UUID
    """Unique identifier for the block."""

    parent: Optional[Parent] = UNSET
    """A Parent object represents the parent of a page, database, or block. The parent can be a workspace, page,
    database, or block."""

    type_: Type1OrStr = Field(alias="type")
    """The type of block. Determines which type-specific content field is present. Common types include paragraph,
    heading_1, heading_2, heading_3, bulleted_list_item, numbered_list_item, to_do, toggle, code, image, divider, table,
    and many more."""

    created_time: RFC3339DateTime
    """Date and time when the block was created (ISO 8601)."""

    last_edited_time: RFC3339DateTime
    """Date and time when the block was last edited (ISO 8601)."""

    created_by: Optional[PartialUser] = UNSET
    """A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields."""

    last_edited_by: Optional[PartialUser] = UNSET
    """A partial User object containing only the object type and ID. Used in created_by and last_edited_by fields."""

    archived: Optional[bool] = UNSET
    """Whether the block has been archived."""

    in_trash: Optional[bool] = UNSET
    """Whether the block is in the trash."""

    has_children: bool
    """Whether the block has child blocks nested within it."""


class BlockDict(TypedDict):
    object_: NotRequired[Literal["block"]]
    id: UUID
    parent: NotRequired[Parent | ParentDict]
    type_: Type1OrStr
    created_time: RFC3339DateTime
    last_edited_time: RFC3339DateTime
    created_by: NotRequired[PartialUser | PartialUserDict]
    last_edited_by: NotRequired[PartialUser | PartialUserDict]
    archived: NotRequired[bool]
    in_trash: NotRequired[bool]
    has_children: bool
