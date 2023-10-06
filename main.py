from fastapi import FastAPI
from database.database import engine
from blog import routers, models

app = FastAPI()
app.include_router(routers.router)


models.Base.metadata.create_all(engine)