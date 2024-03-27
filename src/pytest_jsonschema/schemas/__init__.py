from pathlib import Path

import json


def load(schema_name: str) -> dict:
    """Load data from string."""
    base_path = Path(__file__).parent / f"{schema_name}.json"
    return json.loads(base_path.read_text())
