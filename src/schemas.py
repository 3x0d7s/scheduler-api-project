import datetime
from typing import Optional

from pydantic import BaseModel


class TimedBaseModel(BaseModel):
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
