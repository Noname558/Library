from typing import Optional
from pydantic import BaseModel, Field
from database.BaseModel.AuthorsModel import AuthorSchema
from database.BaseModel.GenresModel import GenreSchema

class BookSchema(BaseModel):
    id: Optional[int]
    name_book: str = Field(min_length=10, max_length=20, description='Book name')
    volume_pages: int = Field(description='Volume pages book')
    rating: int = Field(gt=0, lt=11, description='Rating of books')

class Book_content(BookSchema):
    genres: Optional[list[GenreSchema]] = Field(description="Genre id of the book, returned as a comma-separated string")
    authors: Optional[list[AuthorSchema]] = Field(description="Author id of the book, returned as a comma-separated string")



class Book_content_id(BookSchema):
    genres_id: list[int] = Field(..., description="Book genre id")
    authors_id: list[int] = Field(..., description="Book author id")



class BooksSchema(BaseModel):
    books: Optional[list[Book_content]] or Optional[list[BookSchema]] = Field(description="List of models of books")

    class Config:
        orm_mode = True