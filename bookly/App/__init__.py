from fastapi import FastAPI
from contextlib import asynccontextmanager

from App.books.routes import books
from App.authors.routes import authors
from App.db.main import init_db

version = "1"

@asynccontextmanager
async def life_span(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="Book API", 
    version=version, 
    description="A simple book API",
    lifespan=life_span
)


app.include_router(books, prefix=f"/api/{version}/books", tags=["book"])
app.include_router(authors, prefix=f"/api/{version}/authors", tags=["author"])