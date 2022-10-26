from fastapi import APIRouter
from .auth_api import auth_router
from .task_api import task_router

root_router = APIRouter(prefix='/api/v1')
root_router.include_router(auth_router)
root_router.include_router(task_router)
