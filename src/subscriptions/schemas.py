from typing import List

from pydantic import BaseModel

from src.auth.schemas import UserRead
from src.schedules.schemas import ScheduleWithCreatorRead
from src.schemas import TimedBaseScheme, BaseScheme


class SubscriptionBase(BaseScheme):
    pass


class SubscriptionCreate(SubscriptionBase):
    subscriber_id: int
    schedule_id: int


class SubscriptionRead(SubscriptionBase, TimedBaseScheme):
    id: int
    subscribers: List['UserRead'] = []
    schedules: List['ScheduleWithCreatorRead'] = []
