from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

UpdateBlockErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _UpdateBlockError:
    def map(self, response: HttpResponse) -> UpdateBlockErrorBody:
        match response.status_code:
            case 400 | 401 | 404 | 429:
                return decode_json[Error](response)
            case _:
                return RawError(response)


update_block_error_mapper: Final[ErrorMapper[UpdateBlockErrorBody]] = _UpdateBlockError()
