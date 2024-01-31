from fastapi import FastAPI
from .database import engine
from . import models
from .routers import auth, user_operations

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
# for aithenticated endpoints
# app.include_router(user_operations.router)