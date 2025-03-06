from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from App.books.models import Book, BookCreate, BookUpdate

class BookService:
    async def get_books(self, session:AsyncSession):
        statement = select(Book)
        results = await session.exec(statement)
        return results.all()

    async def get_book(self, id: int, session:AsyncSession):
        statement = select(Book).where(Book.id == id)
        result = session.exec(statement)
        return result.first()

    async def create_book(self, book:BookCreate, session:AsyncSession):
        new_book_dict = book.model_dump()
        new_book = Book(**new_book_dict)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    async def update_book(self, id:int, book_update_data:BookUpdate, session:AsyncSession):
        book_to_update = await self.get_book(id, session)
        if book_to_update is not None:
            book_dict = book_update_data.model_dump()
            for k,v in book_dict.items():
                setattr(book_to_update, k, v)
            await session.commit()
            return book_to_update
        else:
            return None
    
    async def delete_book(self, id:int, session:AsyncSession):
        book_to_delete = await self.get_book(id, session)
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return "Ok"
        else: return None