from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .settings import settings

engine = create_engine(settings.db_url, echo=settings.DB_ECHO)

Session = sessionmaker(bind=engine)


def get_db() -> Session:
    return Session
