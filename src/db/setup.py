from collections.abc import AsyncGenerator

import orjson
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from .config import DbConfig


async def build_async_engine(db_config: DbConfig) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(
        db_config.construct_sqlalchemy_url(),
        echo=True,
        echo_pool=db_config.echo,
        pool_size=50,
    )
    yield engine

    await engine.dispose()


def build_async_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return session_factory


async def get_async_session(session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
