import asyncio

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine

from atomskills_org_bot.config import DATABASE_URL
from atomskills_org_bot.db.tables import Base, Location
from atomskills_org_bot.bot.champ_entities import locations, services, options, halls


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
            if await self.is_table_empty(Location):
                await self._init_fill_tables()

    async def _init_fill_tables(self):
        async with self.session_maker() as session:
            async with session.begin():
                session.add_all(halls)
                session.add_all(services)
                await session.flush()
                session.add_all(locations)
                session.add_all(options)
                await session.commit()

    async def add_record(self, new_record) -> Base:
        async with self.session_maker() as session:
            async with session.begin():
                session.add(new_record)
                await session.commit()
                return new_record

    async def get_records(self, model: type[Base], **kwargs):
        query = select(model).where(
            *[
                getattr(model, key) == value
                for key, value in kwargs.items()
            ]
        )
        async with self.session_maker() as session:
            result = await session.execute(query)
            records = result.scalars().all()
        return records

    async def get_record(self, model: type[Base], record_id: int) -> type[Base]:
        return records[0] if (records := (await self.get_records(model, id=record_id))) else None

    async def update_record(self, model, record_id, **kwargs):
        # noinspection PyTypeChecker
        query = update(model).values(**kwargs).where(model.id == record_id)
        async with self.session_maker() as session:
            await session.execute(query)
            await session.commit()

    async def is_table_empty(self, model):
        async with self.session_maker() as session:
            query = select(model)
            result = await session.execute(query)
            return result.scalars().first() is None


db_manager = DBManager()
