from pydantic import BaseModel


class SeasonBase(BaseModel):
    number: int
    year: int


class SeasonCreate(SeasonBase):
    pass


class Season(SeasonBase):
    id: int

    class Config:
        orm_mode = True
