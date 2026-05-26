from __future__ import annotations

import os

import pytest

from qa_automation_api_suite.client import ApiClient


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    """Provide one reusable client for the contract-test session.

    Keeping the base URL in a fixture mirrors a professional QA framework:
    the environment can change without rewriting individual test cases.
    """

    base_url = os.getenv("QA_API_BASE_URL", "https://jsonplaceholder.typicode.com")
    return ApiClient(
        base_url,
        default_headers={
            "Accept": "application/json",
            "User-Agent": "teogame3d-qa-automation-suite/0.1",
        },
    )
