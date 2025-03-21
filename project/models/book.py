class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
class BookModel:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books