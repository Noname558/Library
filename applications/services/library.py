from typing import List, Optional

from sqlalchemy.engine import interfaces
from ssd_libs.components import component
from ssd_libs.messaging import Message, Publisher

from applications import interface
from database.BaseModel import AuthorsModel, BooksModel, GenresModel
from database.Books import Authors, Books, Genres


@component
class LibraryService:
    library_repo: interfaces.ILibraryRepo
    publisher: Optional[Publisher] = None

    def create_author(self, author: AuthorsModel) -> Authors:
        author_dc = Authors(**author.dict())
        self.library_repo.add_object(author_dc)
        msg = {
            'email_message': {
                'txt': 'Появился новый автор',
                'desc': f'{author_dc.surname} {author_dc.name} {author_dc.middlename}'
            }
        }
        self.__publish_message(msg, 'MailEvent')
        return author_dc

    def create_book(self, book: BooksModel) -> Books:
        book_dc = Books(**book.dict())
        self.library_repo.add_object(book_dc)
        msg = {
            'email_message': {
                'txt': 'Появилась новая книга!',
                'desc': f'Название книги: {book_dc.title}'
            }
        }
        self.__publish_message(msg, 'MailEvent')
        return book_dc

    def create_genre(self, genre: GenresModel) -> Genres:
        genre_dc = Genres(**genre.dict())
        self.library_repo.add_object(genre_dc)
        msg = {
            'email_message': {
                'txt': 'Появилась новая книга!',
                'desc': f'Название книги: {genre_dc.title}'
            }
        }

    def get_all_books(self) -> List[Books]:
        return self.library_repo.all_objects(Books)

    def get_all_authors(self) -> List[Authors]:
        return self.library_repo.all_objects(Authors)

    def get_all_genres(self) -> List[Genres]:
        return self.library_repo.all_objects(Genres)

    def __publish_message(self, msg: dict, queue_name: str) -> None:
        if self.publisher is not None:
            self.publisher.publish(Message(queue_name, msg))
