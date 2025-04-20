from pathlib import Path

import json
import logging
import requests


logger = logging.getLogger("schema-updater")

SCHEMAS = (
    (
        "ansible-vars",
        "https://raw.githubusercontent.com/ansible/ansible-lint/main/src/ansiblelint/schemas/vars.json",
    ),
    (
        "ansible",
        "https://raw.githubusercontent.com/ansible/ansible-lint/main/src/ansiblelint/schemas/ansible.json",
    ),
    (
        "docker-compose",
        "https://raw.githubusercontent.com/compose-spec/compose-spec/master/schema/compose-spec.json",
    ),
    ("github-action", "https://json.schemastore.org/github-action.json"),
    ("github-funding", "https://json.schemastore.org/github-funding.json"),
    ("github-issue-config", "https://json.schemastore.org/github-issue-config.json"),
    ("github-issue-forms", "https://json.schemastore.org/github-issue-forms.json"),
    ("github-workflow", "https://json.schemastore.org/github-workflow.json"),
    (
        "gitlab-ci",
        "https://gitlab.com/gitlab-org/gitlab/-/raw/master/app/assets/javascripts/editor/schema/ci.json",
    ),
    ("package", "https://json.schemastore.org/package.json"),
    ("pre-commit-config", "https://json.schemastore.org/pre-commit-config.json"),
    ("pre-commit-hooks", "https://json.schemastore.org/pre-commit-hooks.json"),
    ("prettierrc", "https://json.schemastore.org/prettierrc.json"),
    ("pyproject", "https://json.schemastore.org/pyproject.json"),
    ("tsconfig", "https://json.schemastore.org/tsconfig.json"),
)


def update_schemas():
    """Download latest version for our schemas."""
    schemas_folder = Path(__file__).parent.parent / "schemas"
    for name, source_url in SCHEMAS:
        response = requests.get(source_url)  # noQA: S113
        if response.status_code > 200:
            logger.error(f"Not possible to download {source_url}")
            continue
        content = json.loads(response.content)
        schema_file = schemas_folder / f"{name}.json"
        schema_file.write_text(json.dumps(content, indent=2))
        logger.info(f"Updated schemas/{schema_file.name}")


if __name__ == "__main__":
    logging.basicConfig()
    logger.setLevel(logging.INFO)
    update_schemas()
