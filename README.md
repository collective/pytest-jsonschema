<h1 align="center">pytest-jsonschema</h1>

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/pytest-jsonschema)](https://pypi.org/project/pytest-jsonschema/)
[![Python Version](https://img.shields.io/pypi/pyversions/pytest-jsonschema)](https://pypi.org/project/pytest-jsonschema/)
[![Wheel](https://img.shields.io/pypi/wheel/pytest-jsonschema)](https://pypi.org/project/pytest-jsonschema/)
[![License](https://img.shields.io/pypi/l/pytest-jsonschema)](https://pypi.org/project/pytest-jsonschema/)
[![Status](https://img.shields.io/pypi/status/pytest-jsonschema)](https://pypi.org/project/pytest-jsonschema/)
[![Tests / QA](https://github.com/collective/pytest-jsonschema/actions/workflows/ci.yml/badge.svg)](https://github.com/collective/pytest-jsonschema/actions/workflows/ci.yml)
[![Contributors](https://img.shields.io/github/contributors/collective/pytest-jsonschema)](https://github.com/collective/pytest-jsonschema/graphs/contributors)
[![Stars](https://img.shields.io/github/stars/collective/pytest-jsonschema?style=social)](https://github.com/collective/pytest-jsonschema/stargazers)

</div>

**pytest-jsonschema** is a plugin for [pytest](https://docs.pytest.org) designed to facilitate JSON Schema validations within your test suites. This tool enables you to validate JSON files, strings, and Python objects against predefined JSON Schemas, ensuring your data adheres to expected formats.

## Installation

Install **pytest-jsonschema** using pip / uv from PyPI:

```bash
pip install pytest-jsonschema
```

## Features & Usage

The package introduces three pytest fixtures for validating JSON data:

### `schema_validate_file`

Validates a JSON file located in your test suite directory:

```python
from pathlib import Path

def test_package_json_is_valid(schema_validate_file):
    path = Path("package.json")
    assert schema_validate_file(path=path, schema_name="package")
```

### `schema_validate_string`

Validates a JSON string:

```python
from pathlib import Path

def test_package_json_is_valid(schema_validate_string):
    data = Path("package.json").read_text()
    assert schema_validate_string(data=data, schema_name="package", file_type="json")
```

### `schema_validate`

Validates a Python dictionary representing JSON data:

```python
import json
from pathlib import Path

def test_package_json_is_valid(schema_validate):
    data = json.loads(Path("package.json").read_text())
    assert schema_validate(data=data, schema_name="package")
```

## Requirements

- pytest >= 6.2.0

## Contributing

To contribute to **pytest-jsonschema**, please follow these steps:

1. Clone the repository:

```bash
git clone git@github.com:collective/pytest-jsonschema.git
```

2. Install the package for development:

```bash
make install
```

3. Format the codebase:

```bash
make format
```

4. Run tests:
- To run all tests:
  ```bash
  uv run pytest
  ```
- To stop on the first error and open a pdb session:
  ```
  uv run pytest -x --pdb
  ```

Testing is conducted using [`pytest`](https://docs.pytest.org/en/stable/).

## License 📜

**pytest-jsonschema** is licensed under the [MIT License](./LICENSE).
