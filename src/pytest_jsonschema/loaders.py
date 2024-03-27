from pathlib import Path
from ruamel.yaml import YAML
from typing import Union

import json


try:
    import tomllib  # Python 3.12
except ImportError:
    import tomli as tomllib

yaml = YAML()

_FILETYPES = {
    ".json": "json",
    ".toml": "toml",
    ".yaml": "yaml",
    ".yml": "yaml",
}

_LOADERS = {
    "json": json.loads,
    "toml": tomllib.loads,
    "yaml": yaml.load,
}


def _guess_format(path: Path) -> str:
    """Given a path, try to guess the correct filetype."""
    extension = path.suffix
    return _FILETYPES.get(extension, "")


def data_from_file(path: Path, file_type: str = "") -> Union[dict, list]:
    """Load data from file."""
    path = Path(path)
    if file_type not in _LOADERS:
        file_type = _guess_format(path)
    data = path.read_text()
    return data_from_string(data, file_type)


def data_from_string(data: str, file_type: str) -> Union[dict, list]:
    """Load data from string."""
    loader = _LOADERS.get(file_type)
    return loader(data)
