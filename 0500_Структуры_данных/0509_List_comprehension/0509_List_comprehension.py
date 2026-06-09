"""
0509_List_comprehension
"""
# [выражение for элемент in итератор]
# [выражение for элемент in итератор if условие]
type BookInfo = dict[str, str | int | float | list[str]]

type Books = list[BookInfo]

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


squares_old = []
for x in range(10):
    if x % 2 == 0:
        squares_old.append(x * x)
        
sqares_new = [
    x * x 
    for x in range(10) 
    if x % 2 == 0
]

print(squares_old)
print(sqares_new)        

pairs_old = []
for x in range(3):
    for y in range(3):
        if x != y:
            pairs_old.append((x, y))
            
pairs_new = [
    (x, y)
    for x in range(3)
    for y in range(3)
    if x != y
]

print(pairs_old)
print(pairs_new)