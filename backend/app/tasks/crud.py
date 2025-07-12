from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Task


class TaskCRUD:
    def __init__(self, session: Session):
        self.session = session

    def get_active_task(self) -> list[Task]:
        with self.session() as session:
            tasks: list[Task] = session.execute(select(Task).where(Task.is_done == False)).scalars().all()
        return tasks

