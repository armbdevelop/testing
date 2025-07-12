from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'db'
    DB_PASSWORD: str = 'passworddb'
    DB_NAME: str = 'db'
    DB_DRIVER: str = 'postgresql+psycopg2-binary'
    DB_ECHO: bool = False

    @property
    def db_url(self) -> str:
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()
