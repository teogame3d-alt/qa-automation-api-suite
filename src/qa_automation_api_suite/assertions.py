from __future__ import annotations

from collections.abc import Iterable
from typing import Any

import requests


def assert_status(response: requests.Response, expected_status: int | tuple[int, ...]) -> None:
    """Assert HTTP status while keeping the failure message useful for triage."""

    assert response.status_code in (
        expected_status if isinstance(expected_status, tuple) else (expected_status,)
    ), f"Expected {expected_status}, got {response.status_code}: {response.text[:200]}"


def assert_json_has_keys(payload: dict[str, Any], required_keys: Iterable[str]) -> None:
    """Verify that a JSON object contains the contract keys required by a test."""

    missing = [key for key in required_keys if key not in payload]
    assert not missing, f"Missing required JSON keys: {missing}"


def assert_non_empty_list_with_keys(payload: Any, required_keys: Iterable[str]) -> None:
    """Validate that a list response has at least one item with expected fields."""

    assert isinstance(payload, list), f"Expected list payload, got {type(payload).__name__}"
    assert payload, "Expected non-empty list payload"
    assert_json_has_keys(payload[0], required_keys)
