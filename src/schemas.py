import datetime
from typing import Optional

from pydantic import BaseModel


class BaseScheme(BaseModel):
    # 'orm_mode' has been renamed to 'from_attributes'
    class Config:
        from_attributes = True


class TimedBaseScheme(BaseScheme):
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
