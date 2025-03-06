from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from .services import BookService
from .models import BookPublic, BookCreate, BookUpdate
from App.dependencies import get_session

books = APIRouter()
book_service = BookService()

@books.get("/")
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_books(session)
    return books

@books.get("/{book_id}", status_code=status.HTTP_200_OK, response_model=BookPublic)
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book(book_id, session)
    if book is not None:
        return book
    else:
        raise HTTPException(
            detail=f"No book exists with Id - {book_id}",
            status_code=status.HTTP_404_NOT_FOUND
        )

@books.post("/create", status_code=status.HTTP_200_OK, response_model=BookPublic)
async def create_book(book_data: BookCreate, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data, session)
    return new_book

@books.patch("/{book_id}", response_model=BookPublic)
async def update_book(
    book_data: BookUpdate, 
    book_id: int, 
    session: AsyncSession = Depends(get_session)
):
    book_to_update = await book_service.update_book(book_id, book_data, session)
    if book_to_update is not None:
        return book_to_update
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No book exists with ID of {book_id}"
    )

@books.delete("/{book_id}")
async def delete_book(book_id: int, session: AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_book(book_id, session)
    if book_to_delete is not None:
        return {}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No book exists with ID of {book_id}"
        )