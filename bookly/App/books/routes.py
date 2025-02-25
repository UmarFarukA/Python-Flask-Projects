from fastapi import APIRouter

books = APIRouter()

@books.get("/")
async def get_books():
    pass

@books.get("/{book_id}")
async def get_book(book_id: int):
    pass

@books.post("/create")
async def create_book():
    pass

@books.patch("/{book_id}")
async def update_book(book_id: int):
    pass

@books.delete("/{book_id}")
async def delete_book(book_id: int):
    pass