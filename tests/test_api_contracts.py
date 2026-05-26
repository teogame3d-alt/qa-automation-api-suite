"""API automation tests for QA portfolio.

Why this style:
- I kept tests deterministic and readable so a mentor/recruiter can review fast.
- Pattern is based on common QA API smoke/contract checks used in pytest + requests.
- Each test validates one behavior: status, contract keys, or negative path.
"""

from qa_automation_api_suite.assertions import (
    assert_json_has_keys,
    assert_non_empty_list_with_keys,
    assert_status,
)
from qa_automation_api_suite.client import ApiClient


def test_get_post_by_id_contract(api_client: ApiClient) -> None:
    # Smoke + contract check: endpoint is up and returns required keys.
    response = api_client.get("/posts/1")
    assert_status(response, 200)
    body = response.json()
    assert_json_has_keys(body, ("userId", "id", "title", "body"))
    assert body["id"] == 1


def test_get_users_list_integrity(api_client: ApiClient) -> None:
    # List integrity check: API should return a non-empty list with core user fields.
    response = api_client.get("/users")
    assert_status(response, 200)
    users = response.json()
    assert_non_empty_list_with_keys(users, ("id", "name", "username", "email"))


def test_create_post_response_shape(api_client: ApiClient) -> None:
    # Basic create flow: verify create endpoint behavior and response contract.
    payload = {"title": "qa smoke", "body": "api test", "userId": 1}
    response = api_client.post("/posts", payload)
    assert_status(response, (200, 201))
    body = response.json()
    assert_json_has_keys(body, ("id", "title", "body", "userId"))


def test_negative_route_returns_404(api_client: ApiClient) -> None:
    # Negative-path check: unknown route should fail predictably with 404.
    response = api_client.get("/definitely-not-existing-route")
    assert_status(response, 404)
