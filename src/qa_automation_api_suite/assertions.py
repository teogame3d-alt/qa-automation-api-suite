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


def assert_json_field_types(payload: dict[str, Any], expected_types: dict[str, type | tuple[type, ...]]) -> None:
    """Validate required JSON field types with triage-friendly failures."""

    assert_json_has_keys(payload, expected_types.keys())
    mismatches = {
        key: type(payload[key]).__name__
        for key, expected_type in expected_types.items()
        if not isinstance(payload[key], expected_type)
    }
    assert not mismatches, f"Unexpected JSON field types: {mismatches}"


def assert_non_empty_list_with_keys(payload: Any, required_keys: Iterable[str]) -> None:
    """Validate that a list response has at least one item with expected fields."""

    assert isinstance(payload, list), f"Expected list payload, got {type(payload).__name__}"
    assert payload, "Expected non-empty list payload"
    assert_json_has_keys(payload[0], required_keys)


def assert_response_time_under(response: requests.Response, max_ms: int) -> None:
    """Check a practical response-time budget without hiding the measured value."""

    elapsed_ms = response.elapsed.total_seconds() * 1000
    assert elapsed_ms <= max_ms, f"Expected response under {max_ms} ms, got {elapsed_ms:.1f} ms"


def assert_header_contains(response: requests.Response, header_name: str, expected_value: str) -> None:
    """Assert a response header contains an expected value fragment."""

    actual = response.headers.get(header_name, "")
    assert expected_value.lower() in actual.lower(), (
        f"Expected {header_name} to contain {expected_value!r}, got {actual!r}"
    )
