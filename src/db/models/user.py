from typing import List

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.models import TimedBaseModel
from src.db.models.follow_entry import FollowerAssociation


class User(SQLAlchemyBaseUserTable[int], TimedBaseModel):
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)

    schedules:      Mapped[list["Schedule"]] = relationship(back_populates="creator")

    follow_entries: Mapped[List["FollowEntry"]] = relationship(
        secondary="follower_association", back_populates="follower"
    )

    follower_associations: Mapped[List["FollowerAssociation"]] = relationship(
        back_populates="follower"
    )

