from typing import Optional, List
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

db = {
    "seasons": []
}

class Season(BaseModel):
    id: int
    name: str
    description: Optional[str]


@router.get("/seasons", response_model=List[Season])
async def get_seasons():
    return db["seasons"]


@router.post("/seasons")
async def create_season(season: Season):
    db["seasons"].append(season)
    return True


@router.get("/seasons/{id}")
async def get_season():
    return True


@router.get("/seasons/{id}/episodes")
async def get_episodes_from_season():
    return True


@router.get("/seasons/{id}/paintings")
async def get_paintings_from_season():
    return True
