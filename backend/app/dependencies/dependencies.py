from fastapi import Depends
from sqlalchemy.orm import Session
from core import get_db
from tasks.crud import TaskCRUD


def get_task_crud(
    db_session: Session = Depends(get_db)
):
    return TaskCRUD(db_session)
