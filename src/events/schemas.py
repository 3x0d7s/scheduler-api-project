import enum
from datetime import time
from typing import Optional

from src.schedules.schemas import ScheduleRead
from src.schemas import TimedBaseModel


class DayOfWeek(enum.Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class EventCreate(TimedBaseModel):
    schedule_id: int
    name: str
    description: Optional[str] = None
    day_of_week: DayOfWeek
    start_time: time
    end_time: time


class EventRead(EventCreate):
    id: int


class EventOfScheduleRead(EventRead):
    schedule: 'ScheduleRead'
