from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import TimedBaseModel

from src.auth.models import User
from src.events.models import Event
from src.subscriptions.models import Subscription, ScheduleAssociation


class Schedule(TimedBaseModel):
    creator_id:     Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    name:           Mapped[str] = mapped_column(nullable=False)
    description:    Mapped[str]

    creator:        Mapped["User"] = relationship(back_populates="schedules")
    events:         Mapped[List["Event"]] = relationship(back_populates="schedule")

    subscriptions: Mapped[List["Subscription"]] = relationship(
        secondary="schedule_association", back_populates="schedule"
    )

    schedule_associations: Mapped[List["ScheduleAssociation"]] = relationship(
        back_populates="schedule"
    )
