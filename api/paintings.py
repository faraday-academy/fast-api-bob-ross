from typing import Optional, List
from fastapi import APIRouter

from schemas.paiting import Painting, PaintColor

router = APIRouter()


@router.get("/paintings", response_model=List[Painting])
async def get_paintings():
    return True


@router.post("/paintings")
async def create_painting(painting: Painting):
    return True


@router.get("/paintings/{id}", response_model=Painting)
async def get_painting():
    return True


@router.get("/paint-colors", response_model=List[PaintColor])
async def get_paint_colors():
    return True


@router.post("/paint-colors")
async def create_painting(paint_color: PaintColor):
    return True
