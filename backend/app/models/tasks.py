from datetime import datetime
from sqlalchemy import Column, Text, String, Boolean, DateTime
from .base import Base


class Task(Base):
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)

    is_done = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
