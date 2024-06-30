from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories import BaseRepo
from src.schedules.models import Schedule
from src.schedules.schemas import ScheduleCreate


class ScheduleRepo(BaseRepo[Schedule, ScheduleCreate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Schedule, ScheduleCreate)
