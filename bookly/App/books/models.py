from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from App.authors.models import Author


class BookBase(SQLModel):
    title: str = Field(index=True)
    description: str | None
    genre: str
    author_id: int = Field(foreign_key="authors.id")
    created_at: datetime = Field(default=datetime.now()) 
    updated_at: datetime | None = None
    
class Book(BookBase, table=True):
    __tablename__ = 'books'
    id: int = Field(primary_key=True)
    author: "Author" = Relationship(back_populates="books")
    
class BookCreate(BookBase):
    ...
    
class BookPublic(BookBase):
    id: int

class BookUpdate(BookBase):
    title: str | None
    description: str | None
    genre: str | None
    updated_at: datetime = datetime.now()
    