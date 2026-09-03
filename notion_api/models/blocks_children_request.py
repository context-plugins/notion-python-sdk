from __future__ import annotations

from uuid import UUID

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .block import Block, BlockDict


class BlocksChildrenRequest(SdkBaseModel):
    children: list[Block]
    """Array of block objects to append as children. Maximum 100 blocks per request."""

    after: Optional[UUID] = UNSET
    """The ID of an existing block to insert the new children after. If omitted, blocks are appended to the end."""


class BlocksChildrenRequestDict(TypedDict):
    children: list[Block | BlockDict]
    after: NotRequired[UUID]
