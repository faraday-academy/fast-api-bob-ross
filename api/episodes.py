from fastapi import APIRouter

router = APIRouter()


@router.get("/episodes")
async def get_episodes():
    return True


@router.get("/episodes/{id}")
async def get_episode():
    return True

