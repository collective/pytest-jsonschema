from pathlib import Path

import json


def load(schema_name: str) -> dict:
    """Load a bundled JSON Schema by name.

    :param schema_name: Name of the schema, without the ``.json`` extension.
    :returns: The parsed JSON Schema.
    :raises FileNotFoundError: If no schema is bundled under that name.
    """
    base_path = Path(__file__).parent / f"{schema_name}.json"
    return json.loads(base_path.read_text())
