from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncSession
from App.config import config


engine = AsyncSession(
    create_engine(
        url=config.DATABASE_URL,
        echo=True
    )
)


async def init_db():
    async with engine.begin() as conn:
        # Create tables and import relevant models
        await conn.run_sync(SQLModel.metadata.create_all)