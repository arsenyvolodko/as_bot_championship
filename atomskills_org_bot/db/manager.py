import asyncio

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

from atomskills_org_bot.config import DATABASE_URL
from atomskills_org_bot.db.tables import Base


class EngineManager:
    def __init__(self, path: str) -> None:
        self.path = path

    async def __aenter__(self) -> AsyncEngine:
        self.engine = create_async_engine(self.path, echo=True)
        return self.engine

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.engine.dispose()


class DBManager:
    def __init__(self):
        self.session_maker = None
        asyncio.run(self._init())

    async def _init(self):
        async with EngineManager(DATABASE_URL) as engine:
            self.session_maker = async_sessionmaker(engine, expire_on_commit=False)
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)

    async def add_record(self, new_record) -> Base:
        async with self.session_maker() as session:
            async with session.begin():
                session.add(new_record)
                await session.commit()
                return new_record

    async def get_record(self, model, record_id):
        # noinspection PyTypeChecker
        query = select(model).where(model.id == record_id)
        async with self.session_maker() as session:
            result = await session.execute(query)
            user = result.scalars().first()
        return user

    async def update_record(self, model, record_id, **kwargs):
        # noinspection PyTypeChecker
        query = update(model).values(**kwargs).where(model.id == record_id)
        async with self.session_maker() as session:
            await session.execute(query)
            await session.commit()


db_manager = DBManager()
