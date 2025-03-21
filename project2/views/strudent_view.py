class StudentView:
    def display_students(self, students):
        if len(students) > 0:
            for student in students:
                print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
        else:
            print("No students found")
    
    def get_student_info(self):
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        return name, age, grade

    def get_update_info(self):
        name = input("Enter updated student name: ")
        new_age = int(input("Enter updated student age: "))
        new_grade = input("Enter updated student grade: ")
        return name, new_age, new_grade
    
    def get_delete_name(self):
        name = input("Enter student name to delete: ")
        return name