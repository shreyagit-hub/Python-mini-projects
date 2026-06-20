'''a university system with students, teachers, and staff members'''

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id, major):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.major = major
    
    def study(self):
        print(f"{self.name} is studying {self.major}")
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        print("-" * 40)

class Teacher(Person):
    def __init__(self, name, age, address, employee_id, subject):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")
        print("-" * 40)

class Staff(Person):
    def __init__(self, name, age, address, staff_id, department):
        super().__init__(name, age, address)
        self.staff_id = staff_id
        self.department = department
    
    def work(self):
        print(f"{self.name} works in {self.department}")
    
    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Department: {self.department}")
        print("-" * 40)

#create university members
print("UNIVERSITY PERSON MANAGEMENT SYSTEM\n")
student = Student("Rita Kumari", 20, "Kathmandu", "S001", "Computer Science")
teacher = Teacher("Prof. Khadka", 45, "Bajhang", "T001", "Data Structures")
staff = Staff("Shyam Bahadur", 40, "Chitwan", "ST001", "Administration")

print("STUDENT:")
student.display_info()
student.study()

print("\nTEACHER:")
teacher.display_info()
teacher.teach()

print("\nSTAFF:")
staff.display_info()
staff.work()