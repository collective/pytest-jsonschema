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
def test_schema_validate_file(
    pytester, resources_folder, base_path, schema_name, expected
):
    path = resources_folder / base_path
    pytester.makepyfile(
        f"""
        def test_schema_validate_file(schema_validate_file):
            assert schema_validate_file(path="{path}", schema_name="{schema_name}") is {expected}
        """
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


@pytest.mark.parametrize(
    "base_path,schema_name,file_type,expected",
    [
        ["valid/github-workflow-changelog.yml", "github-workflow", "yaml", True],
        ["valid/github-workflow-code.yml", "github-workflow", "yaml", True],
        ["valid/github-workflow-lint.yml", "github-workflow", "yaml", True],
        ["valid/package.json", "package", "json", True],
        ["valid/tsconfig.json", "tsconfig", "json", True],
        ["invalid/github-workflow-changelog.yml", "github-workflow", "yaml", False],
        ["invalid/github-workflow-code.yml", "github-workflow", "yaml", False],
        ["invalid/github-workflow-lint.yml", "github-workflow", "yaml", False],
        ["invalid/package.json", "package", "json", False],
        ["invalid/tsconfig.json", "tsconfig", "json", False],
    ],
)
def test_schema_validate_string(
    pytester, resources_folder, base_path, schema_name, file_type, expected
):
    path = resources_folder / base_path
    pytester.makepyfile(
        f"""
        from pathlib import Path


        def test_schema_validate_string(schema_validate_string):

            data = Path("{path}").read_text()
            assert schema_validate_string(data=data, schema_name="{schema_name}", file_type="{file_type}") is {expected}
        """
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


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
def test_schema_validate(pytester, resources_folder, base_path, schema_name, expected):
    path = resources_folder / base_path
    pytester.makepyfile(
        f"""
        from pytest_jsonschema.loaders import data_from_file


        def test_schema_validate(schema_validate):

            data = data_from_file("{path}")
            assert schema_validate(data=data, schema_name="{schema_name}") is {expected}
        """
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
