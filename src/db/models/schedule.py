from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db.models.base import TimedBaseModel
from src.db.models.follow_association import follower_association_table


class Schedule(TimedBaseModel):
    creator_id:     Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    name:           Mapped[str] = mapped_column(nullable=False)
    description:    Mapped[str]

    creator:        Mapped["User"] = relationship(back_populates="schedule")
    events:         Mapped[list["Event"]] = relationship(back_populates="schedule")
    follow_entries: Mapped[list["FollowEntry"]] = relationship(
        secondary=follower_association_table, back_populates="followed"
    )