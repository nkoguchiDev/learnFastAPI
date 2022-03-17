from app.core.config import settings

from neomodel import config

auth = f"{settings.GRAPH_DB_USER}:{settings.GRAPH_DB_PASSWORD}"
config.DATABASE_URL = f'bolt://{auth}@{settings.GRAPH_DB_HOST}:{settings.GRAPH_DB_PORT}'
