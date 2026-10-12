from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

UpdateBlockErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateBlockError:
    def map(self, status_code: int, content: bytes) -> UpdateBlockErrorBody:
        match status_code:
            case 400 | 401 | 404 | 429:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


update_block_error_mapper: Final[ErrorMapper[UpdateBlockErrorBody]] = _UpdateBlockError()
