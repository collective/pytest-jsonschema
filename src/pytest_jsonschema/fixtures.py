from . import loaders
from . import schemas
from . import types
from . import validator

import pytest


@pytest.fixture
def schema_validate_file() -> types.FileValidator:
    """Validate a file againstt a known JSON Schema."""

    def func(path: types.StrPath, schema_name: str, file_type: str = "") -> bool:
        """Validate a file against a known JSON Schema."""
        data = loaders.data_from_file(path, file_type=file_type)
        schema = schemas.load(schema_name)
        return validator.validate(data, schema)

    return func


@pytest.fixture
def schema_validate_string() -> types.StrValidator:
    """Validate a string againstt a known JSON Schema."""

    def func(data: str, schema_name: str, file_type: str = "") -> bool:
        """Validate a string against a known JSON Schema."""
        parsed = loaders.data_from_string(data, file_type=file_type)
        schema = schemas.load(schema_name)
        return validator.validate(parsed, schema)

    return func


@pytest.fixture
def schema_validate() -> types.Validator:
    """Validate a string againstt a known JSON Schema."""

    def func(data: types.DataStructure, schema_name: str) -> bool:
        """Validate a file against a known JSON Schema."""
        schema = schemas.load(schema_name)
        return validator.validate(data, schema)

    return func
