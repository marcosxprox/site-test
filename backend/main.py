import os

from fastapi import FastAPI
from starlette.responses import FileResponse

from . import models, database
from .routers import users

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)

# Caminho absoluto da página HTML
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_PATH = os.path.abspath(os.path.join(BASE_DIR, "frontend", "pagina1.html"))

@app.get("/")
def serve_frontend():
    return FileResponse(FRONTEND_PATH)