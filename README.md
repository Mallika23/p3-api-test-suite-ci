# API Test Suite + CI

[![tests](https://github.com/Mallika23/p3-api-test-suite-ci/actions/workflows/tests.yaml/badge.svg)](https://github.com/Mallika23/p3-api-test-suite-ci/actions/workflows/tests.yaml)

A REST API regression suite built with **Python + pytest + requests**, covering happy paths, negative cases and JSON Schema response validation — running automatically in GitHub Actions on every push and pull request.

## What it covers

| Area | Details |
|---|---|
| CRUD coverage | `GET`, `POST`, `PUT`, `DELETE` against the [reqres.in](https://reqres.in) API |
| Negative testing | Bad payloads, missing fields, unexpected status codes |
| Contract testing | Response bodies validated against a JSON Schema (`jsonschema`) |
| Fixtures | pytest fixtures for setup/teardown isolation between tests |
| CI | GitHub Actions workflow runs the full suite on every push and PR |
| Secrets | API key injected from a GitHub Actions secret — never committed |

## Project structure

```
.
├── .github/workflows/tests.yaml   # CI pipeline
├── test_reqres.py                 # CRUD + negative API tests
├── jsonschema_test.py             # response schema validation
├── test_pytest_main.py            # pytest fundamentals / fixtures
└── pytest_main.py
```

## Running locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install requests jsonschema pytest

export REQRES_API_KEY=your_key   # Windows: set REQRES_API_KEY=your_key
pytest -v
```

## CI

`.github/workflows/tests.yaml` runs on every push and pull request:
checkout → set up Python 3.11 → install dependencies → run the API suite → run the schema suite.
The API key is read from the `REQRES_API_KEY` repository secret, so no credentials live in the repository.

## Why this exists

A compact reference implementation of the API-testing patterns I use day to day — request/response assertions, schema-level contract checks, data-driven cases, and a CI gate that blocks a merge when the contract breaks.
