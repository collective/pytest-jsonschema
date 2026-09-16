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

The package bundles a set of commonly used schemas — for `pyproject.toml`, `package.json`, GitHub Actions workflows, `docker-compose.yml` and more — so you can assert that the configuration files in your own repository are valid, without any network access at test time.

## Installation

Install **pytest-jsonschema** from PyPI:

```bash
pip install pytest-jsonschema
```

Or, with [uv](https://docs.astral.sh/uv/):

```bash
uv add --dev pytest-jsonschema
```

The plugin registers itself with pytest automatically; no configuration is required.

## Usage

The package introduces three pytest fixtures for validating JSON data. Each takes a `schema_name` from the [bundled schemas](#available-schemas) and returns `True` when the data is valid.

### `schema_validate_file`

Validates a file on disk. The format is inferred from the file extension:

```python
from pathlib import Path


def test_package_json_is_valid(schema_validate_file):
    path = Path("package.json")
    assert schema_validate_file(path=path, schema_name="package")
```

Because the format is inferred, this also works for the TOML and YAML files the bundled schemas cover:

```python
from pathlib import Path


def test_pyproject_is_valid(schema_validate_file):
    assert schema_validate_file(path=Path("pyproject.toml"), schema_name="pyproject")


def test_workflow_is_valid(schema_validate_file):
    path = Path(".github/workflows/ci.yml")
    assert schema_validate_file(path=path, schema_name="github-workflow")
```

Pass `file_type` explicitly when the extension does not match the content.

### `schema_validate_string`

Validates a string. There is no filename to infer from, so `file_type` is **required**:

```python
from pathlib import Path


def test_package_json_is_valid(schema_validate_string):
    data = Path("package.json").read_text()
    assert schema_validate_string(data=data, schema_name="package", file_type="json")
```

> [!WARNING]
> If `file_type` is omitted or is not one of the supported values, the string is
> parsed as an empty document rather than raising, and validation will most
> likely return `True`. Always pass `file_type` to this fixture.

### `schema_validate`

Validates an already-parsed Python object — a `dict` or a `list`:

```python
import json
from pathlib import Path


def test_package_json_is_valid(schema_validate):
    data = json.loads(Path("package.json").read_text())
    assert schema_validate(data=data, schema_name="package")
```

## Supported file formats

`schema_validate_file` and `schema_validate_string` accept the following `file_type` values:

| `file_type` | Extensions inferred | Parser |
| --- | --- | --- |
| `json` | `.json` | `json` (standard library) |
| `toml` | `.toml` | `tomllib` (`tomli` below Python 3.12) |
| `yaml` | `.yaml`, `.yml` | [`ruamel.yaml`](https://yaml.readthedocs.io/) |

## Available schemas

Pass one of these as `schema_name`:

| `schema_name` | Validates | Source |
| --- | --- | --- |
| `ansible` | Ansible playbooks | [ansible-lint](https://github.com/ansible/ansible-lint) |
| `ansible-vars` | Ansible variable files | [ansible-lint](https://github.com/ansible/ansible-lint) |
| `docker-compose` | `compose.yml` / `docker-compose.yml` | [compose-spec](https://github.com/compose-spec/compose-spec) |
| `github-action` | `action.yml` for a composite action | [SchemaStore](https://www.schemastore.org/) |
| `github-funding` | `.github/FUNDING.yml` | [SchemaStore](https://www.schemastore.org/) |
| `github-issue-config` | `.github/ISSUE_TEMPLATE/config.yml` | [SchemaStore](https://www.schemastore.org/) |
| `github-issue-forms` | GitHub issue form templates | [SchemaStore](https://www.schemastore.org/) |
| `github-workflow` | `.github/workflows/*.yml` | [SchemaStore](https://www.schemastore.org/) |
| `gitlab-ci` | `.gitlab-ci.yml` | [GitLab](https://gitlab.com/gitlab-org/gitlab) |
| `package` | `package.json` | [SchemaStore](https://www.schemastore.org/) |
| `pre-commit-config` | `.pre-commit-config.yaml` | [SchemaStore](https://www.schemastore.org/) |
| `pre-commit-hooks` | `.pre-commit-hooks.yaml` | [SchemaStore](https://www.schemastore.org/) |
| `prettierrc` | `.prettierrc` | [SchemaStore](https://www.schemastore.org/) |
| `pyproject` | `pyproject.toml` | [SchemaStore](https://www.schemastore.org/) |
| `repository-v1` | `repository.toml`, spec 1 | [repoplone](https://github.com/plone/repoplone) |
| `repository-v2` | `repository.toml`, spec 2 | [repoplone](https://github.com/plone/repoplone) |
| `tsconfig` | `tsconfig.json` | [SchemaStore](https://www.schemastore.org/) |

`repository.toml` has two specifications, and they are not interchangeable: a file
without a `spec_version` key, or with `spec_version = "1"`, is spec 1 and declares
packages as `[backend.package]` / `[frontend.package]` tables; `spec_version = "2"`
declares them as a flat `[[package]]` array. Pick the schema that matches the file:

```python
from pathlib import Path
from pytest_jsonschema.loaders import data_from_file


def test_repository_toml_is_valid(schema_validate_file):
    path = Path("repository.toml")
    spec = str(data_from_file(path).get("spec_version", "1"))
    schema_name = "repository-v2" if spec.startswith("2") else "repository-v1"
    assert schema_validate_file(path=path, schema_name=schema_name)
```

The bundled copies are refreshed with `make update-schemas`.

## Requirements

- Python >= 3.10
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

4. Run the linters and type checks:

   ```bash
   make lint
   ```

5. Run the tests:

   ```bash
   make test
   ```

   To stop on the first error and open a pdb session:

   ```bash
   uv run pytest -x --pdb
   ```

6. Add a change log entry under `news/`, named `<issue-number>.<type>`, where
   `type` is one of `breaking`, `feature`, `bugfix`, `internal`, `documentation`
   or `tests`. Preview the result with `make changelog`.

Run `make help` to see every available target. Testing is conducted using [`pytest`](https://docs.pytest.org/en/stable/).

## License

**pytest-jsonschema** is licensed under the [MIT License](./LICENSE).
