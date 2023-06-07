from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field, root_validator

from database.BaseModel.GenresModel import GenreSchema


class AuthorSchema(BaseModel):
    id: Optional[int] = Field(description='id Author')
    name_author: str = Field(min_length=7, max_length=30, description='Name Author')
    surname: str = Field(min_length=10, max_length=30, description="Author surname")
    patronymic: str = Field(min_length=10, max_length=30, description="Author patronymic")
    date_of_birth: date = Field(..., description="Author date of birth")
    date_of_death: date = Field(description="Author date of death")

    @root_validator
    def date_validate(self, v):
        if v['date_of_birth'] > datetime.now().date():
            raise ValueError('Date of birth must be before the current moment')
        if v['date_of_death'] > v['date_of_birth'] and v['date_of_death'] is not None:
            raise ValueError('Date of death must be before the date of birth')
        return

    class Config:
        orm_mode: True


class Author_content(AuthorSchema):
    from database.BaseModel.BooksModel import BookSchema
    genres: Optional[list[GenreSchema]] = Field(description="List of genres in which the author writes field")
    books: Optional[list[BookSchema]] = Field(description="List of books by this author field")


class AuthorsSchema(BaseModel):
    authors: Optional[list[Author_content]] or Optional[list[AuthorSchema]] = Field(description='List Authors')

    class Config:
        orm_mode: True
