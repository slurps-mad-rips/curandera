from dataclasses import dataclass
from pathlib import Path
from enum import Enum

from typing import Text, List, Optional, TypeVar

Value = TypeVar("Value", bool, Text, Path, None)


class Type(Enum):
    BOOL = 1
    FILEPATH = 2
    PATH = 3
    STRING = 4
    INTERNAL = 5
    STATIC = 6
    UNINITIALIZED = 7


@dataclass
class Entry:
    name: Text
    value: Value
    # properties
    type: Type
    advanced: Optional[bool]
    help: Optional[Text]
    strings: List[Text]


class Cache:
    entries: List[Entry]
