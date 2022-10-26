from fastapi import APIRouter, Depends, Response
from helpers import request

from services.auth import auth_wrapper
from schemas import task, auth
from starlette import status
from settings import settings

task_router = APIRouter(prefix='/task', tags=['task'], )


@task_router.get("/",
                 description='Получение списка всех задач пользователя',
                 responses={200: {"model": task.TaskResponse}},
                 status_code=status.HTTP_200_OK)
async def get_list_task(user=Depends(auth_wrapper)):
    url = settings.TASK_BACKEND_SERVICE.rstrip('/') + '/task/'
    result = await request.request(url, 'get', params={'user_id': user.id})
    return Response(content=result.content, status_code=result.status_code, media_type="application/json")


@task_router.get("/{task_id}",
                 description='Получение конкретной задачи по id',
                 responses={200: {"model": task.TaskResponse}},
                 status_code=status.HTTP_200_OK)
async def get_task(task_id: int, user=Depends(auth_wrapper)):
    url = f"{settings.TASK_BACKEND_SERVICE.rstrip('/')}/task/{task_id}"
    result = await request.request(url, 'get', params={'user_id': user.id})
    return Response(content=result.content, status_code=result.status_code, media_type="application/json")


@task_router.post("/",
                  description='Добавление новой задачи',
                  responses={200: {"model": task.TaskResponse}},
                  status_code=status.HTTP_201_CREATED)
async def add_task(new_task: task.CreateTaskRequest, user: auth.User = Depends(auth_wrapper)):
    url = f"{settings.TASK_BACKEND_SERVICE.rstrip('/')}/task/"
    new_task.bind_user(user)
    result = await request.request(url, 'post', data=new_task.dict())
    return Response(content=result.content, status_code=result.status_code, media_type="application/json")


@task_router.delete("/{task_id}",
                    description='Удаление задачи по id',
                    status_code=status.HTTP_404_NOT_FOUND)
async def delete_task(task_id: int, user=Depends(auth_wrapper)):
    url = f"{settings.TASK_BACKEND_SERVICE.rstrip('/')}/task/{task_id}"
    result = await request.request(url, 'delete', params={'user_id': user.id})
    return Response(content=result.content, status_code=result.status_code, media_type="application/json")
