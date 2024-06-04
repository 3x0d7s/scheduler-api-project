from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship, declared_attr

from src.db.models import TimedBaseModel
from src.db.models.follow_association import follower_association_table, followed_association_table


class FollowEntry(TimedBaseModel):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return "follow_entry"

    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    followed_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), nullable=False)

    follower: Mapped[List["User"]] = relationship(
        secondary=follower_association_table, back_populates="follow_entry"
    )

    followed: Mapped[List["Schedule"]] = relationship(
        secondary=followed_association_table, back_populates="follow_entry"
    )


