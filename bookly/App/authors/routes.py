from fastapi import APIRouter, status, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from .models import Author, AuthorCreate, AuthorPublic, AuthorUpdate
from App.dependencies import get_session
from .services import AuthorService

authors = APIRouter()
author_service = AuthorService()

@authors.get("/", response_model=List[AuthorPublic])
async def get_authors(session: AsyncSession = Depends(get_session)):
    authors = await author_service.get_athours(session)
    return authors

# @authors.get("/{author_id}")
# async def get_author(author_id: int):
#     pass

@authors.post("/create", status_code=status.HTTP_201_CREATED, response_model=AuthorPublic)
async def create_author(author_to_create: AuthorCreate, 
                        session: AsyncSession = Depends(get_session)):
    new_author = await author_service.create_author(author_to_create, session)
    return new_author

# @authors.patch("/{author_id}")
# async def update_author(author_id: int):
#     pass

# @authors.delete("/{author_id}")
# async def delete_author(author_id: int):
#     pass