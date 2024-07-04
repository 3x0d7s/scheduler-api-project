import datetime
from typing import Optional

from pydantic import BaseModel


class BaseScheme(BaseModel):
    class Config:
        orm_mode = True


class TimedBaseScheme(BaseScheme):
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
