from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.events.models import Event
from src.events.schemas import EventCreate
from src.repositories import BaseRepo


class EventsRepo(BaseRepo[Event, EventCreate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Event, EventCreate)
