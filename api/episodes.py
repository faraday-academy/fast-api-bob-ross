from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from db.models.episode import Episode
from db.db_setup import SessionLocal
from schemas.episode import Episode as EpisodeSchema

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_episodes_utils(db: Session):
    return db.query(Episode).all()


@router.get("/episodes", response_model=List[EpisodeSchema])
async def get_episodes(db: Session = Depends(get_db)):
    episodes = get_episodes_utils(db)
    return episodes


@router.post("/episodes")
async def create_episode():
    return True


@router.get("/episodes/{id}")
async def get_episode():
    return True
