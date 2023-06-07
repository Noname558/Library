from sqlalchemy import Integer, String, Column, Date, ForeignKey, Table, create_engine, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:1337/demo_project_book")

Base = declarative_base()

Base.metadata.reflect(engine)


class Books(Base):
    # Имя таблицы
    __tablename__ = 'books'

    # Атрибуты таблицы
    id = Column(Integer, primary_key=True)
    name_books = Column(String(20), nullable=False)
    volume_pages = Column(Integer, nullable=False)
    rate = Column(Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id,
                "name_books": self.name_books,
                "volume_pages": self.volume_pages,
                "rate": self.rate}


# Таблица для связи многие к многим
books_authors = Table("books_authors", Base.metadata,
                      Column('book_id', ForeignKey('books.id'), primary_key=True),
                      Column('authors_id', ForeignKey('authors.id', ondelete='CASCADE'), primary_key=True),
                      )


class Authors(Base):
    # Имя Таблицы
    __tablename__ = 'authors'

    # Атрибуты таблицы
    id = Column(Integer, primary_key=True)
    name_author = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    patronymic = Column(String(30), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    date_of_dead = Column(Date, nullable=False)
    book = relationship('Books', secondary=books_authors, backref="Books_Authors",
                        cascade="all, delete", cascade_backrefs=False)

    def to_dict(self):
        return {"id": self.id,
                "name_author": self.name_author,
                "surname": self.surname,
                "patronymic": self.patronymic,
                "date_of_birth": self.date_of_birth,
                "date_of_dead": self.date_of_dead}


# Таблица для связи многие к многим
books_genres = Table("books_genre", Base.metadata,
                     Column('book_id', ForeignKey('books.id'), primary_key=True),
                     Column('genre_id', ForeignKey('genres.id', ondelete='CASCADE'), primary_key=True),
                     )


class Genres(Base):
    # Имя таблицы
    __tablename__ = 'genres'

    # Атрибуты таблицы
    id = Column(Integer, primary_key=True)
    name_genre = Column(String(20), nullable=False)
    short_description = Column(String(60), nullable=False)
    book = relationship('Books', secondary=books_genres, backref="Books_Genres",
                        cascade="all, delete", cascade_backrefs=False)

    def to_dict(self):
        return {"id": self.id,
                "name_genre": self.name_genre,
                "short_description": self.short_description}
