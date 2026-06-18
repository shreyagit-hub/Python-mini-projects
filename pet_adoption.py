class Pet:
    def __init__(self, name, age, breed, adoption_status="Available"):
        self.name = name
        self.age = age
        self.breed = breed
        self.adoption_status = adoption_status
    
    def display_details(self):
        print(f"Pet Name: {self.name}")
        print(f"Age: {self.age} years")
        print(f"Breed: {self.breed}")
        print(f"Status: {self.adoption_status}")
        print("-----------------------------")
    
    def update_adoption_status(self, status):
        self.adoption_status = status
        print(f"{self.name}'s status updated to: {status}")
    
    def is_available(self):
        return self.adoption_status == "Available"

#create pet instances
pet1 = Pet("Max", 3, "Golden Retriever", "Available")
pet2 = Pet("Tom", 2, "Siamese Cat", "Adopted")
pet3 = Pet("Oreo", 1, "Labrador", "Available")

#display pet details and check availability
print("PET ADOPTION SYSTEM\n")
pet1.display_details()
pet2.display_details()
pet3.display_details()

print(f"Is {pet1.name} available? {pet1.is_available()}")
print(f"Is {pet2.name} available? {pet2.is_available()}")
print(f"Is {pet3.name} available? {pet3.is_available()}")
pet2.update_adoption_status("Available")
pet2.display_details()