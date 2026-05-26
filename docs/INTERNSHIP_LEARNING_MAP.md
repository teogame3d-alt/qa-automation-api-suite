# Internship Learning Map

This repository is organized to show how Python training and internship-style practice can become reviewable QA automation work.

## What I Wanted to Prove

- I can structure a Python project with `src/`, `tests/`, docs, and CI.
- I can separate test scenarios from reusable helper code.
- I can write API checks that cover smoke, contract, create-flow, and negative-path behavior.
- I can document QA strategy, not only write test functions.
- I can use research and mentoring feedback while keeping the final result inspectable through tests and clear code.

## Skills Represented

- Python package organization.
- `pytest` fixtures and reusable assertions.
- REST API validation with `requests`.
- JSON response contract checks.
- Negative testing and failure triage.
- GitHub Actions CI.
- Test strategy documentation.
- Agile QA workflow awareness.
- QA metrics awareness.

## Why This Matters for Employers

The project is intentionally not a giant demo. It is a compact repository that lets a reviewer inspect:

- how the tests are named;
- how assertions fail;
- how the API client keeps repeated setup out of tests;
- how documentation connects code to QA process;
- how a junior profile can demonstrate production-minded habits.

## Next Improvements

- Add parametrized tests for multiple endpoints.
- Add schema validation with typed models or JSON schema.
- Add richer reporting output.
- Add mocked API tests for deterministic offline checks.
- Add a small CI badge and screenshot of a passing test run.
