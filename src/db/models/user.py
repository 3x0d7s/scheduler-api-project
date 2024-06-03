from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.db.models.base import TimedBaseModel


class User(TimedBaseModel):
    username:   Mapped[str] = mapped_column(String, unique=True)
    email:      Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password:   Mapped[str] = mapped_column(String, nullable=False)