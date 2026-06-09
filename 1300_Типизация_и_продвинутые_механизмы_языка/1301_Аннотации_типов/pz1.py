type BookId = int
type Author = str
type Tags = list[str]
type Rating = float
type BookInfo = dict[str, str | int | float | list[str]]

type Genre = str
type Books = list[BookInfo]

def create_book(
    book_id: BookId,
    title: str,
    author: Author,
    year: int,
    rating: Rating,
    tags: Tags,
    genre: Genre = "не указан"
) -> BookInfo:
    """Создает и возвращает словарь с информацией о книге"""
    return {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "tags": tags,
        "genre": genre,
    }
    
def find_book(
    books: Books,
    book_id: BookId
) -> BookInfo | None:
    """Ищет книгу по идентификатору и возвращает ее или None"""
    for book in books:
        if book['id'] == book_id:
            return book
    return None

def filter_books_by_rating(
    books: Books,
    min_rating: float
) -> Books:
    """Возвращает список книг с рейтингом не ниже указанного"""
    return [book for book in books if book['rating'] >= min_rating]

# def filter_books_by_rating(
#     books: Books,
#     min_rating: float
# ) -> Books:
#     """Возвращает список книг с рейтингом не ниже указанного"""
#     result: Books = []
#     for book in books:
#         if book['rating'] >= min_rating:
#             result.append(book)
#     return result

def get_average_rating(
    books: Books
) -> float:
    """Вычисляет и возвращает средний рейтинг всех книг"""
    if not books:
        return 0.0
    total_rating = sum(book["rating"] for book in books)
    return total_rating / len(books)
    
# def get_average_rating(
#     books: Books
# ) -> float:
#     """Вычисляет и возвращает средний рейтинг всех книг"""
#     if not books:
#         return 0.0
#     total_rating: float = 0.0
#     for book in books:
#         total_rating = total_rating + book['rating']
#     return total_rating / len(books)

def find_books_by_author(
    books: Books,
    author: str
) -> Books:
    """Возвращает список книг указанного автора"""
    return [book for book in books if book['author'] == author]

# def find_books_by_author(
#     books: Books,
#     author: str
# ) -> Books:
#     """Возвращает список книг указанного автора"""
#     result: Books = []
#     for book in books:
#         if book['author'] == author:
#             result.append(book)
#     return result

def sort_books_by_rating(
    books: list[BookInfo]
) -> Books:
    """Возвращает новый список книг, отсортированный по убыванию рейтинга"""
    return sorted(books, key=lambda book: book['rating'], reverse=True)    

class Library:
    """Класс для управления каталогом книг"""
    def __init__(self) -> None:
        self.books: Books = []
        
    def add_book(self, book: BookInfo) -> None:
        """Добавляет книгу в каталог"""
        self.books.append(book)
        
    def remove_book(self, book_id: BookId) -> BookInfo | None:
        """Удаляет книгу по ID и возвращает ее. Если книга не найдена, возвращает None"""
        book_to_remove = find_book(self.books, book_id)
        if book_to_remove:
            self.books.remove(book_to_remove)
        return book_to_remove
    
    def get_book(self, book_id: BookId) -> BookInfo | None:
        """Возвращает книгу по ID или None, если книга отсутствует"""
        return find_book(self.books, book_id)
    
    def get_books_count(self) -> int:
        """Возвращает количество книг в каталоге"""
        return len(self.books)

    def get_best_book(self) -> BookInfo | None:
        """Возвращает книгу с самым высоким рейтингом или None, если каталог пуст"""
        if not self.books:
            return None
        return max(self.books, key=lambda book: book['rating'])        
    
if __name__ == '__main__':
    book1: BookInfo = create_book(
        book_id=1,
        title="Python 3.12 в действии",
        author="Иван Петров",
        year=2025,
        rating=9.5,
        tags=["python", "backend", "новинка"],
        genre="Программирование"
    )

    book2: BookInfo = create_book(
        book_id=2,
        title="Основы алгоритмов",
        author="Анна Смирнова",
        year=2023,
        rating=8.2,
        tags=["алгоритмы", "computer science"],
        genre="Образование"
    )

    book3: BookInfo = create_book(
        book_id=3,
        title="Мастерство Python",
        author="Иван Петров",
        year=2024,
        rating=9.7,
        tags=["python", "продвинутый"],
        genre="Программирование"
    )

    book4: BookInfo = create_book(
        book_id=4,
        title="История искусств",
        author="Мария Васильева",
        year=2022,
        rating=7.5,
        tags=["искусство", "история"],
        genre="Гуманитарные науки"
    )

    book5: BookInfo = create_book(
        book_id=5,
        title="Введение в машинное обучение",
        author="Сергей Козлов",
        year=2025,
        rating=9.0,
        tags=["машинное обучение", "python", "ai"],
        genre="Технологии"
    )
    
    library = Library()
    all_books = [book1, book2, book3, book4, book5]
    for book in all_books:
        library.add_book(book)
    
    print(library.get_books_count())
    
    found_book = library.get_book(3)
    print(found_book['rating'])
    print(library.get_book(100))
    
    highly_rated: Books = filter_books_by_rating(library.books, 9.0)
    print(len(highly_rated))
    for book in highly_rated:
        print(f"  - {book['title']}: {book['rating']}")
        
    avg_rating = get_average_rating(library.books)
    print(f'{avg_rating:.2f}')
    
    ivan_books: Books = find_books_by_author(library.books, 'Иван Петров')
    print(len(ivan_books))
    for book in ivan_books:
        print(f"  - {book['title']}: {book['rating']}")
    
    print()
    
    sorted_books: Books = sort_books_by_rating(library.books)
    for book in sorted_books:
        print(f"  - {book['title']}: {book['rating']}")
    
    best_book = library.get_best_book()
    print(best_book['title'])
    library.remove_book(1)
    print(library.get_books_count(
        
    ))
    
    removed_book = library.remove_book(2)
    if removed_book:
        print(f"Книга {removed_book['title']} удалена")
    else:
        print("Книга не найдена")
        
    print(library.get_books_count())