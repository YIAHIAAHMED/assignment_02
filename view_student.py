class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled


    def view_student_info(self):
            print(f'Student Id: {self.student_id}')
            print(f'Name: {self.name}')
            print(f'Department: {self.department}')
            print(f'Is_enrolled: {self.is_enrolled}')
        

student1 = Student(101, 'Yiahia', 'CSE', True)
student2 = Student(102, 'Ahmed', 'ME', False)

student1.view_student_info()
student2.view_student_info()