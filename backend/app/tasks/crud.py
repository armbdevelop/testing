from sqlalchemy import select, update
from sqlalchemy.orm import Session
from models import Task
from tasks.schemas import TaskCreate, TaskUpdate


class TaskCRUD:
    def __init__(self, session: Session):
        self.session = session

    def get_active_task(self) -> list[Task]:
        with self.session() as session:
            tasks: list[Task] = session.execute(select(Task).where(Task.is_done == False)).scalars().all()
        return tasks

    def create_task(self, task: TaskCreate):
        task_model = Task(name=task.name, description=task.description, is_done=False)

        with self.session() as session:
            session.add(task_model)
            session.commit()
            return task

    def update_task(self, task: TaskUpdate):
        q = update(Task).where(Task.id == task.id).values(is_done=True).returning(Task.name)

        with self.session() as session:
            task_name = session.execute(q).scalar_one_or_none()
            session.commit()

        return task_name