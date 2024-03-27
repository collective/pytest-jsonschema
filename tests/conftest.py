from pathlib import Path

import pytest


pytest_plugins = "pytester"


@pytest.fixture(scope="session")
def resources_folder():
    return (Path(__file__).parent / "resources").resolve()


@pytest.fixture
def load_data():
    def func(path):
        from pytest_jsonschema.loaders import data_from_file

        data = data_from_file(path)
        return data

    return func


@pytest.fixture
def load_schema():
    def func(schema_name):
        from pytest_jsonschema.schemas import load

        return load(schema_name)

    return func
