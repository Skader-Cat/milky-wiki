import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker

AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=None,
    expire_on_commit=False,
    class_=AsyncSession
)

class DatabaseManager:
    engine = None
    conn = None
    session = None

    async def create_db_engine(self, settings):
        self.engine = create_async_engine(
            url=settings.DatabaseSettings().GET_DB_URL,
            echo=settings.DevelopmentSettings.DEBUG,
        )

        AsyncSessionLocal.configure(bind=self.engine)

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        return self.engine, conn

    async def get_session(self):
        return AsyncSessionLocal(bind=self.engine)

    async def close_engine(self):
        await self.engine.dispose()

    async def __aenter__(self):
        return await self.get_session()

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close_engine()


Base = declarative_base()

