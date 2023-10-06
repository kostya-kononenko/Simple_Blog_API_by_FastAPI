from fastapi import FastAPI
from database import models
from database.database import engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


models.Base.metadata.create_all(engine)