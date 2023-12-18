import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

class DatabaseManager:
    engine = None
    session_factory = None

    async def create_db_engine(self, settings):
        self.engine = create_async_engine(
            url=settings.DatabaseSettings().GET_DB_URL,
            echo=settings.DevelopmentSettings.DEBUG,
            pool_size=settings.DatabaseSettings.DB_POOL_SIZE,
            max_overflow=settings.DatabaseSettings.DB_MAX_OVERFLOW,
            pool_timeout=settings.DatabaseSettings.DB_POOL_TIMEOUT
        )

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        self.session_factory = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def get_session(self):
        return self.session_factory()

    async def close_engine(self):
        await self.engine.dispose()

    async def __aenter__(self):
        return await self.get_session()

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close_engine()


Base = declarative_base()
DB_Manager = DatabaseManager()
