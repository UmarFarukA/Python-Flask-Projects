from sqlmodel import SQLModel, Field
from datetime import date, datetime


class BookBase(SQLModel):
    title: str
    description: str | None
    genre: str
    
class Book(BookBase, table=True):
    __tablename__ = 'books'
    
class BookCreate(BookBase):
    id: int = Field(default=None, primary_key=True)
    created_at: date = Field(default=datetime.now().date())
    
class BookPublic(BookBase):
    pass

class BookUpdate(BookBase):
    title: str | None
    description: str | None
    genre: str | None
    updated_at: date = Field(default=datetime.now().date())
    