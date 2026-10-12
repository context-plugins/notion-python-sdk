from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Object2(str, Enum):
    """Always "user"."""

    USER = "user"

    __str__ = str.__str__


Object2OrStr: TypeAlias = Annotated[Object2 | str, open_enum_validator(Object2)]
