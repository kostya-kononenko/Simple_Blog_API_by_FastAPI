from fastapi import FastAPI
from database.database import engine
from blog import routers, models
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(routers.router)


models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")


origins = ["http://localhost:3000", "http://localhost:3001"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
