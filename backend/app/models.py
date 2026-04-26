from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    desc: Optional[str] = None
    completed: bool = False