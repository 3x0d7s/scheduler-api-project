from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models import TimedBaseModel


class Subscription(TimedBaseModel):
    subscriber_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False, primary_key=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), nullable=False, primary_key=True)

    # association between Subscription -> Subscriber
    subscriber: Mapped["User"] = relationship(back_populates="subscription_associations")

    # association between Subscription -> Schedule
    schedule: Mapped["Schedule"] = relationship(back_populates="subscription_associations")