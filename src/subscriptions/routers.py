from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.setup import get_async_session
from src.subscriptions.repositories import SubscriptionRepo
from src.subscriptions.schemas import SubscriptionCreate

router = APIRouter(
    prefix="/subscriptions",
    tags=["subscriptions"],
)


@router.get("/")
async def get_subscriptions(session: AsyncSession = Depends(get_async_session)):
    repo = SubscriptionRepo(session)

    return await repo.get_all()


@router.get("/{id}")
async def get_subscription(id: int, session: AsyncSession = Depends(get_async_session)):
    repo = SubscriptionRepo(session)

    return await repo.get_by_id(id)


@router.post("/")
async def create_schedule(new_schedule: SubscriptionCreate, session: AsyncSession = Depends(get_async_session)):
    repo = SubscriptionRepo(session)

    await repo.create(new_schedule)
    return {"status": "success"}