import pytest
import time
from faker import Faker
from api_client import ApiClient
from config import BASE_URL

@pytest.fixture
def api_client():
    """Створює та повертає екземпляр клієнта для тестів."""
    return ApiClient(base_url=BASE_URL)

@pytest.fixture
def fake():
    """Фікстура сама викликає Faker і віддає вже готовий набір унікальних даних."""
    return {
        "title": fake.sentence(nb_words=4),
        "body": fake.text(max_nb_chars=100),
        "userId": 1
    }

@pytest.fixture
def sample_post_payload():
    return {
        "title": "Тестовий заголовок",
        "body": "Тесовий текст нової публікації",
        "userId": 1
    }

@pytest.fixture
def created_post(api_client, sample_post_payload):
    """"Create post through client"""
    response = api_client.create_post(data=sample_post_payload)

    """Return parsed Json answers"""
    return response.json()

@pytest.fixture
def clean_post(api_client, sample_post_payload):
    response = api_client.create_post(data=sample_post_payload)
    post_data = response.json()
    post_id = post_data["id"]
    print(f"\n[SETUP] Створено пост з id={post_id}")

    yield post_data

    print(f"\n[TEARDOWN] Видаляємо пост з id={post_id}")
    delete_res = api_client.delete_post(post_id=1)
    assert delete_res.status_code == 200

@pytest.fixture(autouse=True)
def measure_test_time():
    '''Until test'''
    start_time = time.time()

    yield

    duration = time.time() - start_time
    print(f"\n[BENCHMARK] Час виконання: {duration:.3f} сек")