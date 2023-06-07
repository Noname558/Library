from typing import Optional
from pydantic import BaseModel, Field


class GenreSchema(BaseModel):
    id: Optional[int] = Field(description='Genre id')
    name_genre: str = Field(min_length=10, max_length=20, description='Genre name')
    short_description: str = Field(min_length=20, max_length=60, description='Genre short_description')

    class Config:
        orm_mode = True


class GenresSchema(BaseModel):
    genres: Optional[list[GenreSchema]] = Field(description='List of models of genres')

    class Config:
        orm_mode = True
