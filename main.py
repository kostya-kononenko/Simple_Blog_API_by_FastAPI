from fastapi import FastAPI
from database.database import engine
from blog import routers, models
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(routers.router)


models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')
