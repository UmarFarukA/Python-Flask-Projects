from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .models import Author, AuthorCreate, AuthorPublic, AuthorUpdate

class AuthorService:
    async def get_athours(self, session: AsyncSession):
        stm = select(Author)
        results = await session.exec(stm)
        return results.all()
    
    async def get_author(self, id: int, session:AsyncSession):
        stm = select(Author).where(Author.id == id)
        author = await session.exec(stm)
        return author.first()
    
    async def create_author(self, author_create_data:AuthorCreate, session: AsyncSession):
        new_author_dict = author_create_data.model_dump()
        new_author = Author(**new_author_dict)
        session.add(new_author)
        await session.commit()
        await session.refresh(new_author)
        return new_author
    
    async def update_author(self, author_id:int, author_update_data: AuthorUpdate, session:AsyncSession):
        author_to_update = self.get_author(author_id, session)
        if author_to_update is not None:
            author_update_dict = author_update_data.model_dump()
            for k,v in author_update_dict.items():
                setattr(author_to_update, k, v)
            await session.commit()
            return author_to_update
        else:
            return None
    
    async def delete_author(self, author_id: int, session:AsyncSession):
        author_to_delete = self.get_author(author_id, session)
        if author_to_delete is not None:
            await session.delete(author_to_delete)
            await session.commit()
            return "Ok"
        else:
            return None
        