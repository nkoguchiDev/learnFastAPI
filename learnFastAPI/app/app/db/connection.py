from app.core.config import settings

from neomodel import db

auth = f"{settings.GRAPH_DB_USER}:{settings.GRAPH_DB_PASSWORD}"
SessionLocal = db.set_connection(
    f'bolt://{auth}@{settings.GRAPH_DB_HOST}:{settings.GRAPH_DB_PORT}')
