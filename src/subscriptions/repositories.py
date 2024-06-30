from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories import BaseRepo
from src.subscriptions.models import Subscription
from src.subscriptions.schemas import SubscriptionCreate


class SubscriptionRepo(BaseRepo[Subscription, SubscriptionCreate]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Subscription, SubscriptionCreate)
