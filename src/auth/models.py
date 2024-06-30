from typing import List, TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models import TimedBaseModel

from src.schedules.models import Schedule
from src.subscriptions.models import SubscriberAssociation, Subscription


class User(SQLAlchemyBaseUserTable[int], TimedBaseModel):
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)

    schedules:      Mapped[list["Schedule"]] = relationship(back_populates="creator")

    subscriptions: Mapped[List["Subscription"]] = relationship(
        secondary="subscriber_association", back_populates="follower"
    )

    subscriber_associations: Mapped[List["SubscriberAssociation"]] = relationship(
        back_populates="subscriber"
    )