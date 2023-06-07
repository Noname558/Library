from abc import ABC, abstractmethod
from typing import List

from database.Books import Authors, Books, Genres


class ILibraryRepo(ABC):

    @abstractmethod
    def add_object(self, object: Books | Authors | Genres) -> Books | Authors | Genres:
        """Сохраняет переданный объект в БД и возвращает его."""

    @abstractmethod
    def all_objects(self, cls: type(Books | Authors | Genres)) -> List[Books | Authors | Genres]:
        """ Возвращает все записи из таблицы по классу. """
