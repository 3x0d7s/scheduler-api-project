from typing import Generic, TypeVar, Type

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')
V = TypeVar('V')


class BaseRepo(Generic[T, V]):
    def __init__(self,
                 session: AsyncSession,
                 model: Type[T],
                 create_scheme: Type[V]):
        self.session = session
        self.model = model
        self.create_scheme = create_scheme

    async def create(self, scheme: V):
        create_smth = (
            insert(self.model)
            .values(**scheme.dict())
            .returning(self.model)
        )

        result = await self.session.execute(create_smth)
        await self.session.commit()
        return result.scalar_one()

    async def get_all(self):
        select_smth = (
            select(self.model)
        )

        result = await self.session.execute(select_smth)
        return result.scalars().all()

    async def get_by_id(self, id: int):
        select_smth = (
            select(self.model).filter_by(
                id=id
            )
        )

        result = await self.session.execute(select_smth)
        return result.scalar_one_or_none()

    async def delete_by_id(self, id: int):
        query = (
            select(self.model).filter_by(
                id=id
            )
        )

        result = (await self.session.execute(query)).scalar()
        if result:
            await self.session.delete(result)
            await self.session.commit()
