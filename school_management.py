'''a school system using inheritance'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject, employee_id):
        super().__init__(name, age)
        self.subject = subject
        self.employee_id = employee_id
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
    
    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")
        print(f"Employee ID: {self.employee_id}")

class Student(Person):
    def __init__(self, name, age, roll_number, grade):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.grade = grade
    
    def study(self):
        print(f"{self.name} is studying in grade {self.grade}")
    
    def display_info(self):
        super().display_info()
        print(f"Roll Number: {self.roll_number}")
        print(f"Grade: {self.grade}")

#create objects
print("SCHOOL MANAGEMENT SYSTEM\n")
teacher = Teacher("Mr. Johnson", 35, "Mathematics", "T001")
student = Student("Alice", 15, 101, "10th")

print("Teacher Information:")
teacher.display_info()
teacher.teach()

print("\nStudent Information:")
student.display_info()
student.study()