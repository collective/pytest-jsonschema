# Changelog

<!-- You should *NOT* be adding new change log entries to this file.
     You should create a file in the news directory instead.
     For helpful instructions, please see:
     https://6.docs.plone.org/volto/developer-guidelines/contributing.html#create-a-pull-request
-->

<!-- towncrier release notes start -->

## 1.1.0 (2026-09-16)


### New features:

- Added `repository-v1` and `repository-v2` schemas, validating the `repository.toml` file read by [repoplone](https://github.com/plone/repoplone). @ericof [#10](https://github.com/collective/pytest-jsonschema/issues/10)
- Added support for Python 3.14, and test Python 3.15 (pre-release) in CI. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)


### Internal:

- Removed the unused `.flake8` configuration and leftover `.gitignore` entries from an unrelated force push, and corrected the fixture docstrings. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)
- Re-added VS Code workspace settings and extension recommendations, modelled on cookieplone: ruff as formatter and fixer, pytest as the test runner, and the matching extension set. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)
- Moved `dependabot.yml` from the repository root into `.github/`, where GitHub actually reads it, and added the `uv` ecosystem so Python dependencies are kept up to date alongside GitHub Actions. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)
- Exempted Dependabot pull requests and those labeled `skip changelog` from the change log check, and bumped `astral-sh/setup-uv` to v10.1.0. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)
- Modernized GitHub Actions workflows: bumped `actions/checkout` to v7 and `astral-sh/setup-uv` to v7, replaced the non-functional manual `actions/cache` step with `setup-uv`'s built-in caching, and added a `workflow_dispatch` trigger. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)
- Corrected the docstring of `schemas.load`, which described loading data from a string. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)


### Documentation:

- Reworked the README: documented every bundled schema and the supported file formats, warned that `schema_validate_string` needs an explicit `file_type`, added uv install instructions, and expanded the contributing section. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)


### Tests

- Covered the TOML file and string paths, which previously had no tests: `pyproject.toml` is now exercised through `schema_validate_file` and `schema_validate_string` as well as `schema_validate`. @ericof [#10](https://github.com/collective/pytest-jsonschema/issues/10)
- Added tests validating the repository's own `pyproject.toml` and GitHub Actions workflows against the bundled schemas. @ericof [#11](https://github.com/collective/pytest-jsonschema/issues/11)

## 1.0.0 (2025-11-07)


### New features:

- Update schemas. @ericof 


### Bug fixes:

- The host json.schemastore.org has been changed to www.schemastore.org. @ericof [#8](https://github.com/collective/pytest-jsonschema/issues/8)

## 1.0.0b1 (2025-04-20)


### Internal:

- Modernize package, improve mypy support @ericof 

## 1.0.0a2 (2024-03-27)


### Bugfix

- Add MANIFEST.in file [@ericof] [#5](https://github.com/collective/pytest-jsonschema/issue/5)


### Documentation

- Improve README.md with usage information [@ericof] [#4](https://github.com/collective/pytest-jsonschema/issue/4)

## 1.0.0a1 (2024-03-27)


### Feature

- Implement fixture to validate a file against a json schema [@ericof] [#1](https://github.com/collective/pytest-jsonschema/issue/1)
- Implement fixture to validate a string against a json schema [@ericof] [#2](https://github.com/collective/pytest-jsonschema/issue/2)
- Implement fixture to validate a data structure against a json schema [@ericof] [#3](https://github.com/collective/pytest-jsonschema/issue/3)
