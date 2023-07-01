from fastapi import FastAPI

from app.route import router, engine
from database.models import Base, Entity



def get_app():
    app = FastAPI()
    app.include_router(router)
    return app

app = get_app()