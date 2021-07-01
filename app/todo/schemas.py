from pydantic import BaseModel


class TodoItem(BaseModel):
    title: str
    description: str


class TodoItemResponse(BaseModel):
    title: str
    description: str
    id: int
