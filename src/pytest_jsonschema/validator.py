from .types import DataStructure

import jsonschema
import logging


logger = logging.getLogger("pytest-jsonschema")


def validate(data: DataStructure, schema: dict) -> bool:
    """Validate a data structure against a JSON Schema."""
    try:
        jsonschema.validate(data, schema)
    except jsonschema.ValidationError as exc:
        logger.error(f"Validation failed: {exc}")
        validation = False
    else:
        validation = True
    return validation
