from pydantic import BaseSettings


class Settings(BaseSettings):
    # server settings
    # graph database settings
    GRAPH_DB_HOST: str
    GRAPH_DB_PORT: int
    GRAPH_DB_USER: str
    GRAPH_DB_PASSWORD: str


settings = Settings()
