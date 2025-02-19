from pydantic import BaseModel
from typing import List, Optional

class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int

class TaskListResponse(BaseModel):
    tasks: List[TaskResponse]