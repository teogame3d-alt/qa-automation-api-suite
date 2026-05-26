# Test Automation Strategy

## Goal

Build a readable API test automation suite that demonstrates how I approach framework structure, repeatable validation, CI execution, and quality feedback.

## Scope

- Smoke checks for endpoint availability.
- Contract checks for required JSON keys and payload shape.
- Field type checks for important JSON attributes.
- Query-parameter checks for filtered API behavior.
- Response metadata checks such as content type and practical latency budgets.
- Negative-path checks for predictable error behavior.
- Create-flow response validation.
- CI execution through GitHub Actions on push and pull request.

## Framework Structure

- `ApiClient` centralizes base URL handling, default headers, timeouts, query parameters, GET requests, and POST requests.
- Assertion helpers centralize status-code checks, JSON key validation, field type validation, response metadata, and list integrity checks.
- Pytest fixtures provide reusable client setup.
- Tests stay short so reviewers can understand test intent quickly.

## Automation-Focused Test Strategy

- Prefer deterministic tests that are easy to debug.
- Keep one primary behavior per test.
- Separate framework/helper code from test scenarios.
- Keep the target environment configurable with `QA_API_BASE_URL`.
- Use CI to make regression checks repeatable.
- Document test intent so developers and QA team members can review quickly.

## Future Improvements

- Add environment configuration for staging/production-like URLs.
- Add schema validation with JSON Schema or Pydantic.
- Add retry/reporting strategy for unstable external services.
- Add test markers for smoke, contract, regression, and negative tests.
- Add API coverage matrix and defect tracking notes.
