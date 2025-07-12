from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5432
    DB_USER: str = 'dbuser'
    DB_PASSWORD: str = 'passworddb'
    DB_NAME: str = 'dbn'
    DB_DRIVER: str = 'postgresql+psycopg2'
    DB_ECHO: bool = False

    @property
    def db_url(self) -> str:
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?client_encoding=utf8'


settings = Settings()
