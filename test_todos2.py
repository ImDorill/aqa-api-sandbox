import pytest
from api_json import JsonPlaceHolderClient

@pytest.fixture
def api_client():
    return JsonPlaceHolderClient()

def test_get_todos_success(api_client):
    response = api_client.get_user_todos(user_id=1)

    assert response.status_code == 200
    todos = response.json()
    assert len(todos) > 0

    for item in todos:
        assert item["userId"] == 1

def test_filter_completed_todos(api_client):
    response = api_client.get_user_todos(user_id=1)
    completed_todos = [todo for todo in response.json() if todo["completed"] is True]

    assert len(completed_todos) > 0
    assert all(todo["completed"] is True for todo in completed_todos)

def test_get_todos_non_existent_user(api_client):
    response = api_client.get_user_todos(user_id=9999)

    assert response.status_code == 200
    assert response.json() == []