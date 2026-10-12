from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

RetrieveBlockErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _RetrieveBlockError:
    def map(self, status_code: int, content: bytes) -> RetrieveBlockErrorBody:
        match status_code:
            case 401 | 404 | 429:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


retrieve_block_error_mapper: Final[ErrorMapper[RetrieveBlockErrorBody]] = _RetrieveBlockError()
