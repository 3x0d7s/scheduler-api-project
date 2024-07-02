import enum
from datetime import time
from typing import Optional

from pydantic import BaseModel

from src.schemas import TimedBaseModel


class DayOfWeek(enum.Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class EventCreate(BaseModel):
    schedule_id: int
    name: str
    description: Optional[str] = None
    day_of_week: DayOfWeek
    start_time: time
    end_time: time


class EventRead(EventCreate, TimedBaseModel):
    id: int


class EventOfScheduleRead(EventRead):
    schedule: 'ScheduleRead'
