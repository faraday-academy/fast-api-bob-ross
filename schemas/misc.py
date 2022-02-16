from typing import Optional
from pydantic import BaseModel


class QuoteBase(BaseModel):
    text: str


class QuoteCreate(QuoteBase):
    pass


class Quote(QuoteBase):
    id: int

    class Config:
        orm_mode = True


class GuestBase(BaseModel):
    name: str


class GuestCreate(GuestBase):
    pass


class Guest(GuestBase):
    id: int

    class Config:
        orm_mode = True


class AnimalBase(BaseModel):
    name: Optional[str] = None
    species: str


class AnimalCreate(AnimalBase):
    pass


class Animal(AnimalBase):
    id: int

    class Config:
        orm_mode = True
