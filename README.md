# QA Automation API Suite

Recruiter-focused Python QA project for API test automation.

![QA Automation API Suite overview](docs/images/api-suite-overview.png)

## What This Project Demonstrates
- API smoke tests and endpoint health checks
- Response schema/contract assertions
- Negative-path validation (error status behavior)
- CI execution on every push (GitHub Actions)
- Small framework structure: reusable API client, pytest fixture, and assertion helpers
- Automation-focused test strategy, microservices testing plan, Agile QA workflow, and QA metrics documentation
- Post-internship learning translated into reviewable repository structure, docstrings, tests, and QA documentation

## Tech
Python, pytest, requests, GitHub Actions.

## Framework Structure
- `src/qa_automation_api_suite/client.py`: reusable API client wrapper
- `src/qa_automation_api_suite/assertions.py`: reusable assertion helpers
- `tests/conftest.py`: pytest fixture setup
- `tests/test_api_contracts.py`: smoke, contract, create-flow, and negative-path tests
- `docs/`: test strategy, microservices testing plan, Agile workflow, QA metrics

## Visual Review
The screenshot above is an evidence board for the automation scope. It is not a fake product UI;
it summarizes the framework, checks, and CI signal so a reviewer can understand the project before
opening the test files.

## Post-Internship Learning Signals
- Test code is separated from reusable client/assertion helpers.
- Assertions include triage-friendly failure messages.
- Documentation explains automation strategy, microservices thinking, Agile QA workflow, and quality metrics.
- The repository is intentionally small enough for a recruiter or mentor to inspect quickly, while still showing framework thinking.

## Test Scope
- `GET /posts/1`: status and payload shape
- `GET /users`: list integrity and required fields
- `POST /posts`: basic create flow and response contract
- `GET /invalid-route`: expected 404 behavior

## Run Locally
```bash
python -m venv .venv
.venv\Scripts\python -m pip install -U pip
.venv\Scripts\python -m pip install -e .
.venv\Scripts\python -m pytest
```

## Why It Matters for QA Roles
This repository is intentionally dedicated to automated API validation and repeatable CI checks,
separate from product/UI projects.

## Mentor Notes
See MENTOR_NOTES.md for QA-oriented reasoning, design tradeoffs, and learning summary.

## Learning Map
See `docs/INTERNSHIP_LEARNING_MAP.md` for the connection between SkillBrain/Python learning, QA automation practice, and portfolio evidence.

