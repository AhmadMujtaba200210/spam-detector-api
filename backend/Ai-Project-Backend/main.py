from fastapi import FastAPI
from logic import predict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/spam/{text}")
async def say_hello(text: str):
    return predict(text)