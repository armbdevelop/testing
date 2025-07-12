from typing import List, Annotated
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from dependencies import get_task_crud
from models import Task
from .crud import TaskCRUD

router = APIRouter(prefix="/i_can_do_it", tags=["i_can_do_it"])


@router.get(
    "/get_active_task",
)
def get_active_task(
    taskC: Annotated[TaskCRUD, Depends(get_task_crud)],
):
    try:
        result = taskC.get_active_task()
        return {'result': result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




