from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.db.models import TimedBaseModel
from src.db.models.follow_association import follower_association_table


class User(SQLAlchemyBaseUserTable[int], TimedBaseModel):
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)

    schedules:      Mapped[list["Schedule"]] = relationship(back_populates="user")
    follow_entries: Mapped[list["FollowEntry"]] = relationship(
        secondary=follower_association_table, back_populates="follower")