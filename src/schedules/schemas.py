from typing import Optional, List

from src.auth.schemas import UserRead
from src.events.schemas import EventRead
from src.schemas import TimedBaseModel
from src.subscriptions.schemas import SubscriptionRead


class ScheduleCreate(TimedBaseModel):
    name: str
    creator_id: int
    description: Optional[str] = None


class ScheduleRead(ScheduleCreate):
    id: int

    creator: UserRead


class ScheduleWithEventsRead(ScheduleRead):
    events: List[EventRead] = []
    subscriptions: List[SubscriptionRead] = []
