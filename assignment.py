#1. Create the StudentDatabase class

#Solution Code:
class StudentDatabase:
        student_list = []

        @classmethod
        def add_student(cls, student):
            cls.student_list.append(student)



#2. Create the Student class

#Solution Code:
class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled


#3. Initialize Student Object

#Solution Code:

