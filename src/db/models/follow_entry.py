from typing import List

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship, declared_attr

from src.db.models import TimedBaseModel, BaseModel


class FollowerAssociation(BaseModel):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return "follower_association"

    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    follow_entry_id: Mapped[int] = mapped_column(ForeignKey("follow_entry.follower_id"), primary_key=True)

    # association between Association -> User
    follower: Mapped["User"] = relationship(back_populates="follower_associations")
    # association between Association -> FollowEntry
    follow_entry: Mapped["FollowEntry"] = relationship(back_populates="follower_associations")


class FollowedAssociation(BaseModel):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return "followed_association"

    followed_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), primary_key=True)
    follow_entry_id: Mapped[int] = mapped_column(ForeignKey("follow_entry.followed_id"), primary_key=True)

    # association between Association -> Schedule
    followed: Mapped["Schedule"] = relationship(back_populates="followed_associations")
    # association between Association -> FollowEntry
    follow_entry: Mapped["FollowEntry"] = relationship(back_populates="followed_associations")


class FollowEntry(TimedBaseModel):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return "follow_entry"

    follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False, primary_key=True, unique=True)
    followed_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), nullable=False, primary_key=True, unique=True)

    follower: Mapped[List["User"]] = relationship(
        secondary="follower_association", back_populates="follow_entries"
    )

    follower_associations: Mapped[List["FollowerAssociation"]] = relationship(
        back_populates="follow_entry"
    )

    followed: Mapped[List["Schedule"]] = relationship(
        secondary="followed_association", back_populates="follow_entries"
    )

    followed_associations: Mapped[List["FollowedAssociation"]] = relationship(
        back_populates="follow_entry"
    )



