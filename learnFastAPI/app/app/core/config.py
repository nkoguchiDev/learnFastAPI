from pydantic import BaseSettings


class Settings(BaseSettings):
    MESSAGE: str = "Hello FASTAPI"


settings = Settings()
