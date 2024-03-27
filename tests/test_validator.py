from pytest_jsonschema import validator

import pytest


@pytest.mark.parametrize(
    "base_path,schema_name,expected",
    [
        ["valid/github-workflow-changelog.yml", "github-workflow", True],
        ["valid/github-workflow-code.yml", "github-workflow", True],
        ["valid/github-workflow-lint.yml", "github-workflow", True],
        ["valid/package.json", "package", True],
        ["valid/tsconfig.json", "tsconfig", True],
        ["invalid/github-workflow-changelog.yml", "github-workflow", False],
        ["invalid/github-workflow-code.yml", "github-workflow", False],
        ["invalid/github-workflow-lint.yml", "github-workflow", False],
        ["invalid/package.json", "package", False],
        ["invalid/tsconfig.json", "tsconfig", False],
    ],
)
def test_validate(
    resources_folder, load_data, load_schema, base_path, schema_name, expected
):
    func = validator.validate
    data = load_data(resources_folder / base_path)
    schema = load_schema(schema_name)
    assert func(data, schema) is expected
