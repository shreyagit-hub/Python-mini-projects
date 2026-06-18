'''a library system where users can borrow and return books'''

class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability
    
    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"You have successfully borrowed '{self.title}' by {self.author}")
        else:
            print(f"'{self.title}' is already borrowed. Please try later.")
    
    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"You have successfully returned '{self.title}'")
        else:
            print(f"s'{self.title}' was not borrowed.")
    
    def display_details(self):
        status = "Available" if self.availability else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("\n")

#create book objects
print("LIBRARY BOOK BORROWING SYSTEM\n")
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

print("Initial Library Status:")
book1.display_details()
book2.display_details()
book3.display_details()

print("\nBorrowing Books:")
book1.borrow_book()
book2.borrow_book()
book2.borrow_book()

print("\nLibrary Status After Borrowing:")
book1.display_details()
book2.display_details()

print("\nReturning Books:")
book1.return_book()
book2.return_book()

print("\nFinal Library Status:")
book1.display_details()
book2.display_details()