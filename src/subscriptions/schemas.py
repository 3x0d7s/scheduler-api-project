from typing import List

from pydantic import BaseModel

from src.schemas import TimedBaseModel


class SubscriptionCreate(BaseModel):
    subscriber_id: int
    schedule_id: int


class SubscriptionRead(SubscriptionCreate, TimedBaseModel):
    id: int
    subscribers: List['UserRead'] = []
    schedules: List['ScheduleRead'] = []
