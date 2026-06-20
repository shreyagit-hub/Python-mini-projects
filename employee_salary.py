'''an employee salary system that protects salary data'''

class Employee:
    def __init__(self, name, department, salary):
        self.name = name  # Public
        self._department = department  # Protected
        self.__salary = salary  # Private
    
    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Department: {self._department}")
        print(f"Salary: Rs.{self.__salary}")
        print("\n")
    
    def update_salary(self, new_salary):
        if new_salary < 0:
            print("Salary cannot be negative!")
        else:
            self.__salary = new_salary
            print(f"Salary updated to Rs.{self.__salary}")
    
    def get_salary(self):
        return self.__salary
    
    def give_raise(self, raise_amount):
        if raise_amount < 0:
            print("Raise amount cannot be negative!")
        else:
            self.__salary += raise_amount
            print(f"Raise of Rs.{raise_amount} applied. New salary: Rs.{self.__salary}")

#employee objects
print("EMPLOYEE SALARY MANAGEMENT SYSTEM\n")
emp1 = Employee("John Smith", "Sales", 50000)
emp2 = Employee("Sarah Johnson", "IT", 75000)
emp3 = Employee("Mike Davis", "HR", 60000)

emp1.display_details()
emp2.display_details()
emp3.display_details()

print("Updating salaries:")
emp1.update_salary(55000)
emp2.update_salary(-1000)  #invalid case
emp3.give_raise(5000)

print("\nFinal Details:")
emp1.display_details()
emp2.display_details()
emp3.display_details()