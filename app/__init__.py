from app import config

from fastapi import FastAPI
from .database import engine
from .database import Base
from . import models

from .routers import auth, user_operations

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CHOP.ZIP", version="0.1.1", description="A simple file manager")

app.include_router(auth.router)
# for aithenticated endpoints
app.include_router(user_operations.router)