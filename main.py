from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

from api import seasons, episodes
from db.db_setup import SessionLocal, engine
from db.models.episode import Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(seasons.router)
app.include_router(episodes.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# /paintings
@app.get("/paintings")
async def get_paintings():
    return True


@app.get("/paintings/{id}")
async def get_painting():
    return True


# /colors
@app.get("/colors")
async def get_colors():
    return True
