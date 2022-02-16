from typing import Optional

from pydantic import BaseModel


class EpisodeBase(BaseModel):
    season_id: int
    number: int
    title: str
    description: Optional[str] = None
    youtube_url: str
    date: str


class EpisodeCreate(EpisodeBase):
    pass


class Episode(EpisodeBase):
    id: int

    class Config:
        orm_mode = True
