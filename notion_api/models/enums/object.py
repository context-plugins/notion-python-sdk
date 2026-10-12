from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Object(str, Enum):
    """Always "list" for paginated responses."""

    LIST = "list"

    __str__ = str.__str__


ObjectOrStr: TypeAlias = Annotated[Object | str, open_enum_validator(Object)]
