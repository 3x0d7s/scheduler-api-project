from typing import List

from src.auth.schemas import UserRead
from src.schedules.schemas import ScheduleRead
from src.schemas import TimedBaseModel


class SubscriptionCreate(TimedBaseModel):
    subscriber_id: int
    schedule_id: int


class SubscriptionRead(SubscriptionCreate):
    id: int
    subscribers: List[UserRead] = []
    schedules: List[ScheduleRead] = []