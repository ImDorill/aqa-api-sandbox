import pytest
from api_client import ApiClient
from schemas.post_schema import PostSchema


def test_create_post_success(api_client, sample_post_payload):
    response = api_client.create_post(data=sample_post_payload)
    
    assert response.status_code == 201
    data = response.json()
    
    assert data["title"] == sample_post_payload["title"]
    assert data["body"] == sample_post_payload["body"]
    assert data["userId"] == sample_post_payload["userId"]
    assert "id" in data

def test_get_existing_post(api_client):
    
    # Перевіряємо отримання вже існуючого поста з id=1
    response = api_client.get_post_by_id(post_id=1)
    assert response.status_code == 200

    post = PostSchema.model_validate(response.json())

    assert post.id == 1
    assert post.user_id == 1
    assert len(post.title) > 0

def test_non_existing_post(api_client):
    response = api_client.get_post_by_id(post_id=9999)
    assert response.status_code == 404
    assert response.json() == {}

def test_delete_post(api_client):
    response = api_client.delete_post(post_id=1)
    assert response.status_code == 200

def test_update_post(api_client):
    response = api_client.update_post(
        post_id=1,
        title="Оновлений заголовок",
        body="Оновлений текст поста",
        user_id=1
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Оновлений заголовок"
    assert data["body"] == "Оновлений текст поста"
    assert data["id"] == 1

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_multi_post(api_client, post_id):
    response = api_client.get_post_by_id(post_id=post_id)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert "title" in data

def test_post_lifecycle_e2e(api_client, sample_post_payload):
    response = api_client.create_post(data=sample_post_payload)

    assert response.status_code == 201
    assert "id" in response.json()

    post_id = 1
    response = api_client.update_post(
        post_id=post_id,
        title="Оновлений заголовок",
        body="Я замахався виправляти по 100 раз тести",
        user_id=1
    )
    assert response.status_code == 200

    response = api_client.delete_post(post_id=post_id)
    assert response.status_code == 200

def test_get_created_post_details(created_post):
    assert created_post["id"] is not None
    assert created_post["userId"] == 1

def test_post_with_cleanup(clean_post):
    print(f"[TEST] Перевіряємо пост: {clean_post["title"]}")
    assert clean_post["id"] is not None

def test_filter_posts_by_user(api_client):
    target_user_id = 2
    response = api_client.get_posts_by_user(user_id=target_user_id)

    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0

    for post in posts:
        assert post["userId"] == target_user_id

@pytest.mark.parametrize("invalid_id", [0, -1, 9999, "invalid_text"])
def test_get_post_with_invalid_id(api_client, invalid_id):
    response = api_client.get_post_by_id(invalid_id)
    assert response.status_code == 404