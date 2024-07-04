from typing import List, TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.models import TimedBaseModel


class User(SQLAlchemyBaseUserTable[int], TimedBaseModel):
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)

    schedules:      Mapped[list["Schedule"]] = relationship(back_populates="creator", lazy="selectin")

    subscriptions: Mapped[List["Subscription"]] = relationship(
        secondary="subscriber_association", back_populates="subscriber"
    )

    subscriber_associations: Mapped[List["SubscriberAssociation"]] = relationship(
        back_populates="subscriber"
    )
