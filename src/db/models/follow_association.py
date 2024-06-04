from sqlalchemy import Table, Column, ForeignKey

from src.db.models import BaseModel

follower_association_table = Table(
    "follower_association",
    BaseModel.metadata,
    Column("follower_id", ForeignKey("user.id"), primary_key=True),
    Column("follow_entry_id", ForeignKey("follow_entry.id"), primary_key=True),
)

followed_association_table = Table(
    "followed_association",
    BaseModel.metadata,
    Column("followed_id", ForeignKey("schedule.id"), primary_key=True),
    Column("follow_entry_id", ForeignKey("follow_entry.id"), primary_key=True),
)