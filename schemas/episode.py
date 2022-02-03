from typing import List, Optional

from pydantic import BaseModel


class EpisodeBase(BaseModel):
    title: str
    description: Optional[str] = None
    season: int
    date: str


class EpisodeCreate(EpisodeBase):
    pass


class Episode(EpisodeBase):
    id: int

    class Config:
        orm_mode = True
