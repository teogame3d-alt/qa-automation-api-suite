from __future__ import annotations

import pytest

from qa_automation_api_suite.client import ApiClient


@pytest.fixture(scope="session")
def api_client() -> ApiClient:
    """Provide one reusable client for the contract-test session.

    Keeping the base URL in a fixture mirrors a professional QA framework:
    the environment can change without rewriting individual test cases.
    """

    return ApiClient("https://jsonplaceholder.typicode.com")
