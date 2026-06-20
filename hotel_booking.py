'''a hotel booking system that manages different room types'''

class Room:
    def __init__(self, room_number, price, availability=True):
        self.room_number = room_number
        self.price = price
        self.availability = availability
        self.guest_name = None
    
    def book_room(self, guest_name):
        if self.availability:
            self.availability = False
            self.guest_name = guest_name
            print(f"Room {self.room_number} booked successfully for {guest_name}")
            return True
        else:
            print(f"Room {self.room_number} is not available")
            return False
    
    def cancel_booking(self):
        if not self.availability:
            self.availability = True
            guest = self.guest_name
            self.guest_name = None
            print(f"Room {self.room_number} booking cancelled")
            return True
        else:
            print(f"Room {self.room_number} has no active booking")
            return False
    
    def calculate_total_price(self, nights):
        return self.price * nights
    
    def display_details(self):
        status = "Available" if self.availability else "Booked"
        print(f"Room {self.room_number} | Rs. {self.price}/night | Status: {status}")
        if self.guest_name:
            print(f"Guest: {self.guest_name}")

class SingleRoom(Room):
    def __init__(self, room_number, price=500, availability=True):
        super().__init__(room_number, price, availability)
        self.room_type = "Single Room"
    
    def calculate_total_price(self, nights):
        base_price = super().calculate_total_price(nights)
        print(f"Single Room - {nights} nights @ Rs.{self.price}/night = Rs.{base_price}")
        return base_price

class DoubleRoom(Room):
    def __init__(self, room_number, price=1000, availability=True):
        super().__init__(room_number, price, availability)
        self.room_type = "Double Room"
    
    def calculate_total_price(self, nights):
        base_price = super().calculate_total_price(nights)
        print(f"Double Room - {nights} nights @ Rs.{self.price}/night = Rs.{base_price}")
        return base_price

class SuiteRoom(Room):
    def __init__(self, room_number, price=2000, availability=True):
        super().__init__(room_number, price, availability)
        self.room_type = "Suite Room"
    
    def calculate_total_price(self, nights):
        base_price = super().calculate_total_price(nights)
        complimentary = base_price * 0.05
        print(f"Suite Room - {nights} nights @ Rs.{self.price}/night = Rs.{base_price} (+ 5% complimentary = Rs.{complimentary:.2f})")
        return base_price + complimentary

# Hotel booking system
print("HOTEL ROOM BOOKING SYSTEM\n")
single = SingleRoom(101, 500)
double = DoubleRoom(102, 1000)
suite = SuiteRoom(103, 2000)

print("1. Available Rooms:")
single.display_details()
double.display_details()
suite.display_details()

print("\n2. Booking Rooms:")
single.book_room("John Doe")
double.book_room("Jane Smith")

print("\n3. Room Details After Booking:")
single.display_details()
double.display_details()

print("\n4. Calculate Total Price:")
single.calculate_total_price(3)
double.calculate_total_price(2)
suite.calculate_total_price(1)

print("\n5. Cancel Booking:")
single.cancel_booking()

print("\n6. Final Room Status:")
single.display_details()
double.display_details()