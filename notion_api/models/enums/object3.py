from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Object3(str, Enum):
    """Always "error" for error responses."""

    ERROR = "error"

    __str__ = str.__str__


Object3OrStr: TypeAlias = Annotated[Object3 | str, open_enum_validator(Object3)]
