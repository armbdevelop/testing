from typing import List, Annotated
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from dependencies import get_task_crud
from models import Task
from .crud import TaskCRUD
from .schemas import TaskCreate, TaskUpdate

router = APIRouter(prefix="/i_can_do_it", tags=["i_can_do_it"])


@router.get(
    "/get_active_task",
)
def get_active_task(
    taskC: Annotated[TaskCRUD, Depends(get_task_crud)],
):
    """
    Получение всех активных задач
    """
    try:
        result = taskC.get_active_task()
        return {'result': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    "/create_task",
)
def create_task(
    taskC: Annotated[TaskCRUD, Depends(get_task_crud)],
    task: TaskCreate,
):
    """
        Создание задачи, автоматом она будет считаться как активная
    """
    try:
        result = taskC.create_task(task)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.patch(
    "/update_task",
)
def update_task(
    taskC: Annotated[TaskCRUD, Depends(get_task_crud)],
    task: TaskUpdate,
):
    """
    Обновляет задачу, делает ее выполненной
    Возвращает имя задачи
    """
    try:
        result = taskC.update_task(task)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
