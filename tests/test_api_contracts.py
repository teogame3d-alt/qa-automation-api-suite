"""API automation tests for QA portfolio.

Why this style:
- I kept tests deterministic and readable so a mentor/recruiter can review fast.
- Pattern is based on common QA API smoke/contract checks used in pytest + requests.
- Each test validates one behavior: status, contract keys, or negative path.
"""

from qa_automation_api_suite.assertions import (
    assert_header_contains,
    assert_json_field_types,
    assert_json_has_keys,
    assert_non_empty_list_with_keys,
    assert_response_time_under,
    assert_status,
)
from qa_automation_api_suite.client import ApiClient


def test_get_post_by_id_contract(api_client: ApiClient) -> None:
    # Smoke + contract check: endpoint is up and returns required keys.
    response = api_client.get("/posts/1")
    assert_status(response, 200)
    assert_response_time_under(response, 5000)
    assert_header_contains(response, "Content-Type", "application/json")
    body = response.json()
    assert_json_field_types(
        body,
        {
            "userId": int,
            "id": int,
            "title": str,
            "body": str,
        },
    )
    assert body["id"] == 1


def test_get_users_list_integrity(api_client: ApiClient) -> None:
    # List integrity check: API should return a non-empty list with core user fields.
    response = api_client.get("/users")
    assert_status(response, 200)
    users = response.json()
    assert_non_empty_list_with_keys(users, ("id", "name", "username", "email"))
    assert_json_field_types(users[0], {"id": int, "name": str, "username": str, "email": str})


def test_query_filter_returns_only_requested_user_posts(api_client: ApiClient) -> None:
    # Query parameter check: filtered list should keep the requested relationship.
    response = api_client.get("/posts", params={"userId": 1})
    assert_status(response, 200)
    posts = response.json()
    assert_non_empty_list_with_keys(posts, ("userId", "id", "title", "body"))
    assert all(post["userId"] == 1 for post in posts)


def test_create_post_response_shape(api_client: ApiClient) -> None:
    # Basic create flow: verify create endpoint behavior and response contract.
    payload = {"title": "qa smoke", "body": "api test", "userId": 1}
    response = api_client.post("/posts", payload)
    assert_status(response, (200, 201))
    body = response.json()
    assert_json_has_keys(body, ("id", "title", "body", "userId"))
    assert body["title"] == payload["title"]
    assert body["body"] == payload["body"]
    assert body["userId"] == payload["userId"]


def test_negative_route_returns_404(api_client: ApiClient) -> None:
    # Negative-path check: unknown route should fail predictably with 404.
    response = api_client.get("/definitely-not-existing-route")
    assert_status(response, 404)
