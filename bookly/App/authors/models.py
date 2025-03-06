from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from App.books.models import Book, BookBase

class AuthorBase(SQLModel):
    first_name: str = Field(index=True)
    middle_name: str | None
    last_name: str
    qualification: str | None
    country: str | None
    created_at: datetime = Field(default=datetime.now())
    updted_at: datetime = Field(default=None, nullable=True)
    
    
class Author(AuthorBase, table=True):
    __tablename__ = "authors"
    id: int = Field(default=None, primary_key=True)
    books: List['Book'] = Relationship(back_populates="authors")
    
class AuthorPublic(AuthorBase):
    id: int
    
class AuthorCreate(AuthorBase):
    ...
    
class AuthorUpdate(AuthorBase):
    first_name: str | None
    middle_name: str | None
    last_name: str | None
    qualification: str | None
    country: str | None
    updted_at: datetime = datetime.now()