from pathlib import Path
from typing import Protocol
from typing import TypeAlias
from typing import Union


StrPath: TypeAlias = Union[str, Path]
DataStructure = Union[dict, list]


class FileValidator(Protocol):
    def __call__(self, path: StrPath, schema_name: str, file_type: str = "") -> bool:
        ...


class StrValidator(Protocol):
    def __call__(self, data: str, schema_name: str, file_type: str = "") -> bool:
        ...


class Validator(Protocol):
    def __call__(self, data: DataStructure, schema_name: str) -> bool:
        ...
