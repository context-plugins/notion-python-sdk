from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error import Error

DeleteBlockErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteBlockError:
    def map(self, status_code: int, content: bytes) -> DeleteBlockErrorBody:
        match status_code:
            case 401 | 404 | 429:
                return decode_json[Error](content)
            case _:
                return RawError(status_code, content)


delete_block_error_mapper: Final[ErrorMapper[DeleteBlockErrorBody]] = _DeleteBlockError()
