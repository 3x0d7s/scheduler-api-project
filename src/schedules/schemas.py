from typing import Optional, List, TYPE_CHECKING

from pydantic import BaseModel

from src.schemas import TimedBaseModel

from src.auth.schemas import UserRead
from src.events.schemas import EventRead
from src.subscriptions.schemas import SubscriptionRead


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
