from fastapi import FastAPI

app = FastAPI()

"""
app.{HTTPメソッド}("{resource path}")
def 関数名
  return {response body}
"""


@app.get("/hello")
def hello():
    return {"message": "Hello World"}
