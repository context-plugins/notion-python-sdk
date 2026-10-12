from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

RetrieveBlockChildrenErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RetrieveBlockChildrenError:
    def map(self, status_code: int, content: bytes) -> RetrieveBlockChildrenErrorBody:
        match status_code:
            case 401 | 404 | 429:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


retrieve_block_children_error_mapper: Final[ErrorMapper[RetrieveBlockChildrenErrorBody]] = _RetrieveBlockChildrenError()
