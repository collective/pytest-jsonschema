from pathlib import Path
from typing import Protocol


StrPath = str | Path
DataStructure = dict | list


class FileValidator(Protocol):
    def __call__(
        self, path: StrPath, schema_name: str, file_type: str = ""
    ) -> bool: ...


class StrValidator(Protocol):
    def __call__(
        self, raw_data: str, schema_name: str, file_type: str = ""
    ) -> bool: ...


class Validator(Protocol):
    def __call__(self, data: DataStructure, schema_name: str) -> bool: ...
