from fastapi import FastAPI

from app.core.config import settings

app = FastAPI()


@app.get("/message")
def hello():
    return {"msg": f"{settings.MESSAGE}"}
