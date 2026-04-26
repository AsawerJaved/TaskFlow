from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    desc: str = None

class TaskUpdate(BaseModel):
    title: str = None
    desc: str = None
    completed: bool = None