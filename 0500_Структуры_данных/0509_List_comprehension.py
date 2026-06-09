"""
0509_List_comprehension
"""
# [выражение for элемент in итератор]
# [выражение for элемент in итератор if условие]
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


