from sqlmodel import create_engine, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine

from App.config import config


engine = AsyncEngine(
    create_engine(
        url=config.DATABASE_URL,
        echo=True
    )
)


async def init_db() -> None:
    async with engine.begin() as conn:
        from App.authors.models import Author
        from App.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)