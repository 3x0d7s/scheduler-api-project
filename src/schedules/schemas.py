from typing import Optional, List

from pydantic import BaseModel

from src.schemas import TimedBaseModel


class ScheduleCreate(BaseModel):
    name: str
    creator_id: int
    description: Optional[str] = None


class ScheduleRead(ScheduleCreate, TimedBaseModel):
    id: int

    creator: 'UserRead'


class ScheduleWithEventsRead(ScheduleRead):
    events: List['EventRead'] = []
    subscriptions: List['SubscriptionRead'] = []
