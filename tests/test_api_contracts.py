"""Basic API automation tests for QA portfolio.

Why this style:
- I kept tests deterministic and readable so a mentor/recruiter can review fast.
- Pattern is based on common QA API smoke/contract checks used in pytest + requests.
- Each test validates one behavior: status, contract keys, or negative path.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_by_id_contract() -> None:
    # Smoke + contract check: endpoint is up and returns required keys.
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)
    assert response.status_code == 200
    body = response.json()
    for key in ("userId", "id", "title", "body"):
        assert key in body
    assert body["id"] == 1


def test_get_users_list_integrity() -> None:
    # List integrity check: API should return a non-empty list with core user fields.
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    sample = users[0]
    for key in ("id", "name", "username", "email"):
        assert key in sample


def test_create_post_response_shape() -> None:
    # Basic create flow: verify create endpoint behavior and response contract.
    payload = {"title": "qa smoke", "body": "api test", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    assert response.status_code in (200, 201)
    body = response.json()
    for key in ("id", "title", "body", "userId"):
        assert key in body


def test_negative_route_returns_404() -> None:
    # Negative-path check: unknown route should fail predictably with 404.
    response = requests.get(f"{BASE_URL}/definitely-not-existing-route", timeout=10)
    assert response.status_code == 404
