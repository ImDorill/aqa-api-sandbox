import requests

class JsonPlaceHolderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_user_todos(self, user_id: int) -> requests.Response:
        return requests.get(f"{self.BASE_URL}/todos", params={"userId": user_id})