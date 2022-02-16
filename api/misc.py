from typing import Optional, List
from fastapi import APIRouter

from schemas.misc import Quote, Guest, Animal

router = APIRouter()


@router.get("/quotes", response_model=List[Quote])
async def get_quotes():
    return True


@router.post("/quotes")
async def create_quote(quote: Quote):
    return True


@router.get("/guests", response_model=List[Guest])
async def get_guests():
    return True


@router.post("/guests")
async def create_guest(guest: Guest):
    return True


@router.get("/animals", response_model=List[Animal])
async def get_animals():
    return True


@router.post("/animals")
async def create_animal(animal: Animal):
    return True
