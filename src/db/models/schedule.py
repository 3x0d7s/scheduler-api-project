from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import TimedBaseModel


class Schedule(TimedBaseModel):
    creator_id:     Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    name:           Mapped[str] = mapped_column(nullable=False)
    description:    Mapped[str]

    creator:        Mapped["User"] = relationship(back_populates="schedules")
    events:         Mapped[List["Event"]] = relationship(back_populates="schedule")

    follow_entries: Mapped[List["FollowEntry"]] = relationship(
        secondary="followed_association", back_populates="followed"
    )

    followed_associations: Mapped[list["FollowedAssociation"]] = relationship(
        back_populates="followed"
    )
