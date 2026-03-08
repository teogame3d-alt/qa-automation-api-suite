# QA Automation API Suite

Recruiter-focused Python QA project for API test automation.

## What This Project Demonstrates
- API smoke tests and endpoint health checks
- Response schema/contract assertions
- Negative-path validation (error status behavior)
- CI execution on every push (GitHub Actions)

## Tech
Python, pytest, requests, GitHub Actions.

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
