class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
class StudentModel:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def get_students(self):
        return self.students

    def update_student(self, name, new_age, new_grade):
        for student in self.students:
            if student.name == name:
                student.age = new_age
                student.grade = new_grade
                return
            
    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return
            