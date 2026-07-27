class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled


    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            print(f'{self.name} has been enrolled successfully.')
        else:
            print(f'{self.name} is already enrolled.')

student1 = Student(101, 'Yiahia', 'CSE', True)
student2 = Student(102, 'Ahmed', 'ME', False)

student1.enroll_student()
student2.enroll_student()
