from fastapi import FastAPI, Depends, HTTPException, APIRouter, Request
from sqlalchemy.orm import Session
from . import models, database
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel



router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WindowCreate(BaseModel):
    name: str
    content: str

class FolderCreate(BaseModel):
    name: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(database.get_db)):
    windows = db.query(models.Window).all()
    folders = db.query(models.Folder).all()
    return templates.TemplateResponse("index.html", {"request": request, "windows": windows, "folders": folders})

@router.post("/windows/")
async def create_window(window: WindowCreate, db: Session = Depends(database.get_db)):
    db_window = models.Window(name=window.name, content=window.content)
    db.add(db_window)
    db.commit()
    db.refresh(db_window)
    return db_window

@router.post("/folders/")
async def create_folder(folder: FolderCreate, db: Session = Depends(database.get_db)):
    db_folder = models.Folder(name=folder.name)
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder

app.include_router(router)



app.mount("/static", StaticFiles(directory="app/static"), name="static")