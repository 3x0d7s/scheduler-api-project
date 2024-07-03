from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.events.repositories import EventsRepo
from src.events.schemas import EventCreate
from src.setup import get_async_session

router = APIRouter(
    prefix="/events",
    tags=["events"],
)


@router.get("/")
async def get_events(session: AsyncSession = Depends(get_async_session)):
    repo = EventsRepo(session)

    return await repo.get_all()


@router.get("/{id}")
async def get_event(id: int, session: AsyncSession = Depends(get_async_session)):
    repo = EventsRepo(session)

    return await repo.get_by_id(id)


@router.post("/")
async def create_schedule(new_schedule: EventCreate, session: AsyncSession = Depends(get_async_session)):
    repo = EventsRepo(session)

    await repo.create(new_schedule)
    return {"status": "success"}
