from api_client import ApiClient
from schemas.comment_schema import CommentSchema

def test_get_comments_for_post(api_client):
    response = api_client.get_comments_by_post_id(post_id=1)
    assert response.status_code == 200

    comments = response.json()
    len(comments) > 0

    for item in comments:
        comment = CommentSchema.model_validate(item)
        assert comment.post_id == 1
