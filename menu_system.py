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

    def enroll_student(self):
            if not self.is_enrolled:
                self.is_enrolled = True
                print(f'{self.name} has been enrolled successfully.')
            else:
                print(f'{self.name} is already enrolled.')

    def drop_student(self):
                self.is_enrolled = False
                print(f'{self.name} has dropped out.')

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)
        

student1 = Student(101, 'Yiahia', 'CSE', True)
student2 = Student(102, 'Ahmed', 'ME', False)

student1.view_student_info()
student2.view_student_info()