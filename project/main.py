from models.book import BookModel
from views.book_view import BookView
from controllers.book_controller import BookController

def main():
    model = BookModel()
    view = BookView()
    controller = BookController(model, view)

    while True:
        print("\n1. Add book\n2. Display books\n3. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1": controller.add_book()
            case "2": controller.display_books()
            case "3": break
            case _ : print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()