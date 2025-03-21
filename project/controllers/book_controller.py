from models.book import Book

class BookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_book(self):
        title, author = self.view.get_book_info()
        book = Book(title, author)
        self.model.add_book(book)

    def display_books(self):
        books = self.model.get_books()
        self.view.display_books(books)

