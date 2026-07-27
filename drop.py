class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled


    def drop_student(self):
            self.is_enrolled = False
            print(f'{self.name} has dropped out.')

student1 = Student(101, 'Yiahia', 'CSE', True)

student1.drop_student()
print(student1.is_enrolled)
