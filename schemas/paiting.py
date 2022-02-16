from pydantic import BaseModel

from db.models.painting import PaintingType


class PaintingBase(BaseModel):
    episode_id: int
    title: str
    image_url: str
    type: PaintingType


class PaintingCreate(PaintingBase):
    pass


class Painting(PaintingBase):
    id: int

    class Config:
        orm_mode = True


class PaintColorBase(BaseModel):
    name: str
    hex: str


class PaintColorCreate(PaintColorBase):
    pass


class PaintColor(PaintColorBase):
    id: int

    class Config:
        orm_mode = True
