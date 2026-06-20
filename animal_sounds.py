'''a program where different animals make different sounds using the same method name'''

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says: Meow! Meow!")

class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} says: Moo! Moo!")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} says: Tweet! Tweet!")

# Create animal objects
print("ANIMAL SOUND POLYMORPHISM SYSTEM\n")
animals = [
    Dog("Max"),
    Cat("Tom"),
    Cow("Lali"),
    Bird("Pattu")
]

print("Animals and their sounds:")
for animal in animals:
    animal.make_sound()