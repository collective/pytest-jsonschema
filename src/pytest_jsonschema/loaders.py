from . import types
from collections.abc import Callable
from pathlib import Path
from ruamel.yaml import YAML

import json
import sys


if sys.version_info >= (3, 12):
    import tomllib
else:
    import tomli as tomllib

yaml = YAML()


_FILETYPES: dict[str, str] = {
    ".json": "json",
    ".toml": "toml",
    ".yaml": "yaml",
    ".yml": "yaml",
}

_LOADERS: dict[str, Callable] = {
    "json": json.loads,
    "toml": tomllib.loads,
    "yaml": yaml.load,
}


def _guess_format(path: Path) -> str:
    """Given a path, try to guess the correct filetype."""
    extension = path.suffix
    return _FILETYPES.get(extension, "")


def data_from_file(path: types.StrPath, file_type: str = "") -> dict | list:
    """Load data from file."""
    path = Path(path)
    if file_type not in _LOADERS:
        file_type = _guess_format(path)
    data = path.read_text()
    return data_from_string(data, file_type)


def data_from_string(data: str, file_type: str) -> dict:
    """Load data from string."""
    loader = _LOADERS.get(file_type)
    return loader(data) if loader else {}
