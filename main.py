from fastapi import FastAPI
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer

from logic import predict

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/spam/{text}")
async def say_hello(text: str):
    return predict(text)