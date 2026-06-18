'''a student report card system that calculates marks and grades'''

class Student:
    def __init__(self, name, roll_number, marks1, marks2, marks3):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.total_marks = 0
        self.percentage = 0
        self.grade = ""
    
    def calculate_total(self):
        self.total_marks = self.marks1 + self.marks2 + self.marks3
        return self.total_marks
    
    def calculate_percentage(self):
        self.percentage = (self.total_marks / 300) * 100
        return self.percentage
    
    def calculate_grade(self):
        if self.percentage >= 90:
            self.grade = "A+"
        elif self.percentage >= 80:
            self.grade = "A"
        elif self.percentage >= 70:
            self.grade = "B"
        elif self.percentage >= 60:
            self.grade = "C"
        elif self.percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"
        return self.grade
    
    def print_report_card(self):
        self.calculate_total()
        self.calculate_percentage()
        self.calculate_grade()
        
        print(f"STUDENT REPORT CARD")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Subject 1 Marks: {self.marks1}")
        print(f"Subject 2 Marks: {self.marks2}")
        print(f"Subject 3 Marks: {self.marks3}")
        print(f"Total Marks: {self.total_marks}/300")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.grade}")
        print()

#create student objects
print("STUDENT REPORT CARD SYSTEM\n")
student1 = Student("John Doe", 101, 95, 88, 92)
student2 = Student("Jane Smith", 102, 78, 85, 82)
student3 = Student("Carol White", 103, 65, 70, 68)

student1.print_report_card()
student2.print_report_card()
student3.print_report_card()