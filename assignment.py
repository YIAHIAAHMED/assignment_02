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


#4. Implement enroll_student() method

#Solution Code:
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


#5. Implement drop_student() method

#Solution Code:
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


#6. Implement view_student_info() method

#Solution Code: