class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

class StudentDatabase:
        student_list = []

        @classmethod
        def add_student(cls, student):
            cls.student_list.append(student)

# manually create Student objects
student1 = Student(101, 'Yiahia', 'CSE', True)
student2 = Student(102, 'Ahmed', 'ME', True)

# insert student objects into student_list
StudentDatabase.add_student(student1)
StudentDatabase.add_student(student2)