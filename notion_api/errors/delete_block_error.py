from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.error import Error

DeleteBlockErrorBody: TypeAlias = Error | RawError


@dataclass(frozen=True, slots=True)
class _DeleteBlockError:
    def map(self, response: HttpResponse) -> DeleteBlockErrorBody:
        match response.status_code:
            case 401 | 404 | 429:
                return decode_json[Error](response)
            case _:
                return RawError(response)


delete_block_error_mapper: Final[ErrorMapper[DeleteBlockErrorBody]] = _DeleteBlockError()
