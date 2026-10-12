from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Object1(str, Enum):
    """Always "block" for block objects."""

    BLOCK = "block"

    __str__ = str.__str__


Object1OrStr: TypeAlias = Annotated[Object1 | str, open_enum_validator(Object1)]
