from typing import List
from fastapi import APIRouter

from schemas.season import Season

router = APIRouter()


@router.get("/seasons", response_model=List[Season])
async def get_seasons():
    return True


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
