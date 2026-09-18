from pydantic import BaseModel, Field

class PostSchema(BaseModel):
    id: int
    user_id: int = Field(alias="userId")
    title: str
    body: str