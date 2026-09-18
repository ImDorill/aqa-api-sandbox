import requests

class ApiClient:

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def create_post(self, data: dict) -> requests.Response:
        return requests.post(f"{self.base_url}/posts", json=data)

    def get_post_by_id(self, post_id: int) -> requests.Response:
        url = f"{self.base_url}/posts/{post_id}"
        return requests.get(url)

    def delete_post(self, post_id: int) -> requests.Response:
        url = f"{self.base_url}/posts/{post_id}"
        return requests.delete(url)

    def update_post(self, post_id: int, title: str, body: str, user_id: int) -> requests.Response:
        url = f"{self.base_url}/posts/{post_id}"
        payload = {
                    "title": title,
                    "body": body,
                    "userId": user_id
                }
        return requests.put(url, json = payload)

    def get_user_by_id(self, user_id: int) -> requests.Response:
        url = f"{self.base_url}/users/{user_id}"
        return requests.get(url)

    def get_comments_by_post_id(self, post_id: int) -> requests.Response:
        url = f"{self.base_url}/comments"
        return requests.get(url, params={"postId": post_id})

    def get_todos_by_id(self, todo_id: int) -> requests.Response:
        url = f"{self.base_url}/todos/{todo_id}"
        return requests.get(url)

    def get_posts_by_user(self, user_id: int) -> requests.Response:
        url = f"{self.base_url}/posts"
        return requests.get(url, params={"userId": user_id})