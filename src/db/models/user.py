from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.models import TimedBaseModel
from src.db.models.follow_association import follower_association_table


class User(TimedBaseModel):
    firstname:      Mapped[str] = mapped_column(nullable=False)
    lastname:       Mapped[str] = mapped_column(nullable=False)
    username:       Mapped[str] = mapped_column(nullable=False, unique=True)
    email:          Mapped[str] = mapped_column(nullable=False, unique=True)
    password:       Mapped[str] = mapped_column(nullable=False)

    schedules:      Mapped[list["Schedule"]] = relationship(back_populates="user")
    follow_entries: Mapped[list["FollowEntry"]] = relationship(
        secondary=follower_association_table, back_populates="follower")