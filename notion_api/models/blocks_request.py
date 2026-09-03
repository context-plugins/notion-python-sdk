from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BlocksRequest(SdkBaseModel):
    """Block type-specific content to update. Include the block type key with the fields to modify."""

    archived: Optional[bool] = UNSET
    """Set to true to archive the block."""


class BlocksRequestDict(TypedDict):
    archived: NotRequired[bool]
