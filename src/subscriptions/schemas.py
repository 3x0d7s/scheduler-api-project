from typing import List, TYPE_CHECKING

from src.auth.schemas import UserRead
from src.schedules.schemas import ScheduleRead
from src.schemas import TimedBaseModel

if TYPE_CHECKING:
    from src.auth.schemas import UserRead
    from src.schedules.schemas import ScheduleRead


class SubscriptionCreate(TimedBaseModel):
    subscriber_id: int
    schedule_id: int


class SubscriptionRead(SubscriptionCreate):
    id: int
    subscribers: List['UserRead'] = []
    schedules: List['ScheduleRead'] = []
