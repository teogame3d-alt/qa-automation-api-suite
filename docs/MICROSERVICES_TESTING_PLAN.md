# Microservices Testing Plan

This repository uses a public demo API, but the same testing approach can be extended to microservices architecture.

## What I Would Validate

- Service health and endpoint availability.
- HTTP status codes and error behavior.
- Contract stability between services.
- JSON payload shape and required fields.
- Field type consistency for consumer-facing payloads.
- Query/filter behavior for collection endpoints.
- Response metadata such as content type and practical latency budgets.
- Data consistency between related endpoints.
- Negative paths and invalid input behavior.
- Regression coverage for high-risk flows.

## Microservices Risk Areas

- Contract changes that break consumers.
- Missing required fields.
- Incorrect status codes.
- Slow or unstable dependent services.
- Inconsistent data between service responses.
- Poor error messages for downstream failures.

## TV Ecosystem Example

For a Live and VoD ecosystem, I would design end-to-end checks around:

- Live channel listing.
- VoD catalogue search and details.
- Playback entitlement / availability rules.
- User/session state.
- Error messages when content is unavailable.
- Regression checks for critical customer flows.
