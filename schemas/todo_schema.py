from pydantic import BaseModel, Field

class TodoSchema(BaseModel):
    user_id: int = Field(alias="userId")
    id: int
    title: str
    completed: bool