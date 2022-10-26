from pydantic import BaseModel
from schemas.auth import User


class BaseTaskRequest(BaseModel):
    id: int


class GetTaskRequest(BaseTaskRequest):
    pass


class DeleteTaskRequest(BaseTaskRequest):
    pass


class CreateTaskRequest(BaseModel):
    title: str
    completed: bool = False
    user_id: int = None
    username: str = None

    def bind_user(self, user: User):
        self.user_id = user.id
        self.username = user.username


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    user_id: int
    username: str
