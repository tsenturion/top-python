from models.student import Student

class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def add_student(self):
        name, age, grade = self.view.get_student_info()
        student = Student(name, age, grade)
        self.model.add_student(student)
    
    def display_students(self):
        students = self.model.get_students()
        self.view.display_students(students)
    
    def update_student(self):
        name, new_age, new_grade = self.view.get_student_info()
        self.model.update_student(name, new_age, new_grade)

    def delete_student(self):
        name = self.view.get_delete_name()
        self.model.delete_student(name)
        

    
