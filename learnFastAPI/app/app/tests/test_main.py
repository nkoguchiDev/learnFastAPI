from fastapi.testclient import TestClient

from app.main import app
from app.core.config import settings

client = TestClient(app)


def test_read_main():
    """GET /message へのREST APIコールで、
        1. レスポンスコードが200であること
        2. {"msg": "Hello FASTAPI"}が返却されること
    """
    response = client.get("/message")
    assert response.status_code == 200
    assert response.json() == {"msg": f"{settings.MESSAGE}"}
