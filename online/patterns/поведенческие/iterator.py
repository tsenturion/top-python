"""
iterator
структура:
iterable (коллекция/контейнер)
iterator (итератор)
__iter__()
__next__()
StopIteration

iter()
next()

(+)
разделение коллекции и способа перебора
несколько разных способов перебора
ленивая загрузка данных
единый интерфейс

(-)
увеличивает сложноть кода если обход простой
итераторы обычно не могут быть перебраны несколько раз
не всегда эффективно по памяти
"""
class Library:
    def __init__(self, books):
        self.books = books

    def __iter__(self):
        return LibraryIterator(self.books)

class LibraryIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.books):
            raise StopIteration
        book = self.books[self.index]
        self.index += 1
        return book

library = Library(["1984", "Гарри Поттер", "Игра престолов"])
for book in library:
    print(book)
#-----------------------------------------------------------------
class ReverseLibraryIterator:
    def __init__(self, books):
        self.books = books
        self.index = len(books) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        book = self.books[self.index]
        self.index -= 1
        return book

library = Library(["1984", "Гарри Поттер", "Игра престолов"])
reverse_iterator = ReverseLibraryIterator(library.books)

for book in reverse_iterator:
    print(book)
#-----------------------------------------------------------------
from itertools import zip_longest

class Library:
    def __init__(self, books):
        self.books = books

    def __iter__(self):
        return iter(self.books)

library1 = Library(["Книга A", "Книга B", "Книга C"])
library2 = Library(["Книга 1", "Книга 2"])

for book1, book2 in zip_longest(library1, library2, fillvalue="Нет книги"):
    print(f"{book1} - {book2}")
#-----------------------------------------------------------------
def book_generator(books):
    for book in books:
        yield book

books = ["1984", "Гарри Поттер", "Игра престолов"]
for book in book_generator(books):
    print(book)


def book_generator(books):
    for book in books:
        yield book
        