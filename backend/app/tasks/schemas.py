from pydantic import BaseModel


class TaskCreate(BaseModel):
    name: str
    description: str


class TaskUpdate(BaseModel):
    id: int
