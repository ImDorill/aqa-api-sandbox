from pydantic import BaseModel, Field

class CommentSchema(BaseModel):
    post_id: int =Field(alias="postId")
    id: int
    name: str
    email: str
    body: str