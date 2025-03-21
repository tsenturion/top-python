class BookView:
    def display_books(self, books):
        if len(books) > 0:
            for book in books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books found")

    def get_book_info(self):
        title = input()
        author = input()
        return title, author

        