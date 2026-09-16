"""Validate this repository's own configuration against the bundled schemas.

These tests exercise the plugin the way the README tells users to: by pointing
the fixtures at real configuration files rather than at test resources. They
double as a guard against committing a workflow that the bundled
``github-workflow`` schema rejects.
"""

from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).parent.parent
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"

# ``/.github`` is excluded from the sdist, so these files only exist when the
# tests run against a repository checkout.
pytestmark = pytest.mark.skipif(
    not WORKFLOWS_DIR.is_dir(),
    reason="not a repository checkout: .github is excluded from the sdist",
)

WORKFLOWS = sorted(WORKFLOWS_DIR.glob("*.yml")) if WORKFLOWS_DIR.is_dir() else []


def test_workflows_are_discovered():
    """Guard against the parametrized test below silently covering nothing."""
    assert WORKFLOWS, f"no workflows found in {WORKFLOWS_DIR}"


def test_pyproject_is_valid(schema_validate_file):
    """The project's own pyproject.toml validates against the pyproject schema."""
    path = REPO_ROOT / "pyproject.toml"
    assert schema_validate_file(path=path, schema_name="pyproject")


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda path: path.name)
def test_workflow_is_valid(schema_validate_file, path):
    """Each workflow validates against the github-workflow schema."""
    assert schema_validate_file(path=path, schema_name="github-workflow")
