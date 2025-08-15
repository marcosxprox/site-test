from fastapi import FastAPI
from . import models, database
from .routers import users

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)