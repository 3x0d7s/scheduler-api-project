from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.schedules.repositories import ScheduleRepo
from src.schedules.schemas import ScheduleCreate, ScheduleWithCreatorRead
from src.setup import get_async_session

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"],
)


@router.get("/", response_model=List[ScheduleWithCreatorRead])
async def get_schedules(session: AsyncSession = Depends(get_async_session)):
    repo = ScheduleRepo(session)

    return await repo.get_all()


@router.get("/{id}", response_model=ScheduleWithCreatorRead)
async def get_schedule(id: int, session: AsyncSession = Depends(get_async_session)):
    repo = ScheduleRepo(session)

    return await repo.get_by_id(id)


@router.post("/")
async def create_schedule(new_schedule: ScheduleCreate, session: AsyncSession = Depends(get_async_session)):
    repo = ScheduleRepo(session)

    await repo.create(new_schedule)
    return {"status": "success"}
