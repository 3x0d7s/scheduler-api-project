from typing import Optional, List

from pydantic import BaseModel

from src.auth.schemas import UserRead
from src.schemas import TimedBaseScheme, BaseScheme


class ScheduleBase(BaseModel):
    name: str
    description: Optional[str] = None


class ScheduleCreate(ScheduleBase):
    creator_id: int


class ScheduleRead(ScheduleBase, TimedBaseScheme):
    id: int


class ScheduleWithCreatorRead(ScheduleRead):
    creator: 'UserRead'


class ScheduleWithEventsAndCreatorRead(ScheduleWithCreatorRead):
    events: List['EventRead'] = []
    subscriptions: List['SubscriptionRead'] = []

