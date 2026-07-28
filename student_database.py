# Student StudentDatabase System

#Solution Code:

class StudentDatabase:
        student_list = []

        @classmethod
        def add_student(cls, student):
            cls.student_list.append(student)

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        # private attribute
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        # Add student to student_list
        StudentDatabase.add_student(self)

    # Enroll student
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f'{self.__name} has been enrolled successfully.')
        else:
            print(f'{self.__name} is already enrolled.')
    
    # Drop Student
    def drop_student(self):   
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f'{self.__name} has dropped out.')
        else:
            print(f'Error: {self.__name} is not currently enrolled.')    
            

    # view_student_info() method
    def view_student_info(self):
            print(f'Student Id: {self.__student_id}')
            print(f'Name: {self.__name}')
            print(f'Department: {self.__department}')
            print(f"Enrolled Status: {'Enrolled' if self.__is_enrolled else 'Not Enrolled'}")
            print('-' * 30)

    # Getter for Student ID (For privacy data)

    def get_student_id(self):
         return self.__student_id


# manually create Student objects
student1 = Student(101, 'Yiahia', 'CSE', True)
student2 = Student(102, 'Ahmed', 'ME', True)


# Menu System

while True:
    print('\n-------------------------------\n')
    print('1. View All Students.')
    print('2. Enroll Student.')
    print('3. Drop Student.')
    print('4. Exit.')
    try:
         option = int(input('Enter your option: '))
    except ValueError:
         print('Error: please enter a valid option')
         continue
    

    # Option 1: View All Students
    if option == 1:
        print('\n-------------------------------\n')
        if len(StudentDatabase.student_list) == 0:
             print('No Student Found.')
        else: 
            print('View All Students.')
            for student in StudentDatabase.student_list:
                student.view_student_info()

    # Option 2: Enroll Students
    elif option == 2 :
        try:
             student_id = int(input('Enter Student ID: '))
             flag = False
             for student in StudentDatabase.student_list:
                  if student.get_student_id() == student_id:
                       flag = True
                       student.enroll_student()
                       break
             if not flag:
                  print('Error:  Invalid Student ID.')
             
        except ValueError:
            print('Error: Please enter a valid Student ID.')
    

     # Option 3: Drop Students       
    elif option == 3:
        try:
             student_id = int(input('Enter Student ID: '))
             flag = False
             for student in StudentDatabase.student_list:
                  if student.get_student_id() == student_id:
                       flag = True
                       student.drop_student()
                       break
             if not flag:
                  print('Error:  Invalid Student ID.')
             
        except ValueError:
            print('Error: Please enter a valid Student ID.')

    # Option 4: Exit
    elif option == 4:
        print('Program Exited.')
        break

     # Invalid menu option   
    else:
        print('wrong option. Please select 1-4.\n')  