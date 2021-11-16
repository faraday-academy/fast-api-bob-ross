from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = {
    "seasons": []
}

class Season(BaseModel):
    id: int
    name: str
    description: Optional[str]


@app.get("/")
async def root():
    return {"message": "Hello World"}


# /seasons
@app.get("/seasons", response_model=List[Season])
async def get_seasons():
    return db["seasons"]


@app.post("/seasons")
async def create_season(season: Season):
    db["seasons"].append(season)
    return True


# /seasons/:id
@app.get("/seasons/{id}")
async def get_season():
    return True


# /seasons/:id/episodes
@app.get("/seasons/{id}/episodes")
async def get_episodes_from_season():
    return True


# /seasons/:id/paintings
@app.get("/seasons/{id}/paintings")
async def get_paintings_from_season():
    return True


# /episodes
@app.get("/episodes")
async def get_episodes():
    return True


# /episodes/:id
@app.get("/episodes/{id}")
async def get_episode():
    return True


# /paintings
@app.get("/paintings")
async def get_paintings():
    return True


# /paintings/:id
@app.get("/paintings/{id}")
async def get_painting():
    return True


# /colors
@app.get("/colors")
async def get_colors():
    return True
