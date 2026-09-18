from api_client import ApiClient
from schemas.user_schema import UserSchema

def test_get_users_success(api_client):
    response = api_client.get_user_by_id(user_id=1)
    assert response.status_code == 200

    # data = response.json()
    # len(data) > 0

    user = UserSchema.model_validate(response.json())
    assert user.id == 1
    assert user.username == "Bret"

def test_get_non_exestent_user(api_client):
    response = api_client.get_user_by_id(user_id=9999)
    assert response.status_code == 404