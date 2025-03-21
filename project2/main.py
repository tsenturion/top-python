from models.student import StudentModel
from views.strudent_view import StudentView
from controllers.student_controller import StudentController

def main():
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)

    while True:
        print("\n1. Add student\n2. Display students\n3. Update student\n4. Delete student\n5. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1": controller.add_student()
            case "2": controller.display_students()
            case "3": controller.update_student()
            case "4": controller.delete_student()
            case "5": break
            case _ : print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()