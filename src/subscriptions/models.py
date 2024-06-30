from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship, declared_attr

from src.models import BaseModel, TimedBaseModel

from src.auth.models import User
from src.schedules.models import Schedule


class SubscriberAssociation(BaseModel):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return "subscriber_association"

    subscriber_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscription.subscriber_id"), primary_key=True)

    # association between Association -> User
    subscriber: Mapped["User"] = relationship(back_populates="subscriber_associations")
    # association between Association -> Subscription
    subscription: Mapped["Subscription"] = relationship(back_populates="subscriber_associations")


class ScheduleAssociation(BaseModel):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return "schedule_association"

    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), primary_key=True)
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscription.schedule_id"), primary_key=True)

    # association between Association -> Schedule
    schedule: Mapped["Schedule"] = relationship(back_populates="schedule_associations")
    # association between Association -> Subscription
    subscription: Mapped["Subscription"] = relationship(back_populates="schedule_associations")


class Subscription(TimedBaseModel):
    subscriber_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False, primary_key=True, unique=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), nullable=False, primary_key=True, unique=True)

    subscriber: Mapped[List["User"]] = relationship(
        secondary="subscriber_association", back_populates="subscriptions"
    )

    subscriber_associations: Mapped[List["SubscriberAssociation"]] = relationship(
        back_populates="subscription"
    )

    schedule: Mapped[List["Schedule"]] = relationship(
        secondary="schedule_association", back_populates="subscriptions"
    )

    schedule_associations: Mapped[List["ScheduleAssociation"]] = relationship(
        back_populates="subscription"
    )



