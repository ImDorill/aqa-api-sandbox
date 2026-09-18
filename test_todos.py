import pytest
import allure
from api_client import ApiClient
from schemas.todo_schema import TodoSchema

@allure.feature("Todos Management")
class TestTodos:

    @allure.title("Успішне отримання задачі за валідним ID")
    def test_get_todos_success(self, api_client):
        with allure.step("Надсилаємо GET запит на отримання todo з id=1"):
            response = api_client.get_todos_by_id(todo_id=1)

        with allure.step("Перевіряємо стату коду відповіді (очікуємо 200)"):
            assert response.status_code == 200

        with allure.step("Валідуємо структуру відповіді через Pydantic"):
            todo = TodoSchema.model_validate(response.json())
            assert todo.id == 1
            assert len(todo.title) > 0

    @allure.title("Отримання 404 про невалідному ID задачі")
    @pytest.mark.parametrize("todo_id", [9999, -1, 0, "abc"])
    def test_get_non_existent_todo(self, api_client, todo_id):
        with allure.step(f"Надсилаємо GET запит з невалідним todo_id={todo_id}"):
            response = api_client.get_todos_by_id(todo_id=todo_id)

        with allure.step("Перевіряємо що сервер повернув статус 404"):
            assert response.status_code == 404