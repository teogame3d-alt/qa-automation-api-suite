from __future__ import annotations

from dataclasses import dataclass
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

    def url(self, path: str) -> str:
        """Build a stable endpoint URL from the configured base URL and path."""

        normalized = path if path.startswith("/") else f"/{path}"
        return f"{self.base_url.rstrip('/')}{normalized}"

    def get(self, path: str) -> requests.Response:
        """Send a GET request with the default timeout."""

        return requests.get(self.url(path), timeout=self.timeout)

    def post(self, path: str, payload: dict[str, Any]) -> requests.Response:
        """Send a JSON POST request with the default timeout."""

        return requests.post(self.url(path), json=payload, timeout=self.timeout)
