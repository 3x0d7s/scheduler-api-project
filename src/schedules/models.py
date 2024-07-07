from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import TimedBaseModel


class Schedule(TimedBaseModel):
    creator_id:     Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    name:           Mapped[str] = mapped_column(nullable=False)
    description:    Mapped[str]

    creator:        Mapped["User"] = relationship(back_populates="schedules", lazy="selectin")
    events:         Mapped[List["Event"]] = relationship(back_populates="schedule", lazy="selectin")

    subscribers: Mapped[List["User"]] = relationship(
        secondary="subscription", back_populates="subscriptions", lazy="selectin"
    )

    subscription_associations: Mapped[List["Subscription"]] = relationship(
        back_populates="schedule"
    )
