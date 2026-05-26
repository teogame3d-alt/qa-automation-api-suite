from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import requests


@dataclass(frozen=True)
class ApiClient:
    """Small API client wrapper used by pytest fixtures and tests.

    I keep HTTP details in one place so the test files can read like QA
    scenarios instead of low-level request setup. This is the same separation I
    would expect in a larger automation framework: tests describe behavior,
    helpers handle transport details.
    """

    base_url: str
    timeout: int = 10
    default_headers: dict[str, str] = field(default_factory=dict)

    def url(self, path: str) -> str:
        """Build a stable endpoint URL from the configured base URL and path."""

        normalized = path if path.startswith("/") else f"/{path}"
        return f"{self.base_url.rstrip('/')}{normalized}"

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> requests.Response:
        """Send an HTTP request through one controlled framework path.

        Centralizing transport behavior mirrors a real API test framework:
        timeout, headers, query parameters, and JSON payloads are managed in
        one place instead of being repeated in every test.
        """

        merged_headers = {**self.default_headers, **(headers or {})}
        return requests.request(
            method=method.upper(),
            url=self.url(path),
            params=params,
            json=payload,
            headers=merged_headers,
            timeout=self.timeout,
        )

    def get(self, path: str, *, params: dict[str, Any] | None = None) -> requests.Response:
        """Send a GET request with optional query parameters."""

        return self.request("GET", path, params=params)

    def post(self, path: str, payload: dict[str, Any]) -> requests.Response:
        """Send a JSON POST request with the default timeout."""

        return self.request("POST", path, payload=payload)
