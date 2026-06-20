'''a vehicle rental system for bikes, cars, and scooters'''

class Vehicle:
    def __init__(self, brand, model, rent_price):
        self.brand = brand
        self.model = model
        self.rent_price = rent_price
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Rent Price: Rs.{self.rent_price}/day")
    
    def calculate_rent(self, days):
        return self.rent_price * days

class Car(Vehicle):
    def calculate_rent(self, days):
        base_rent = super().calculate_rent(days)
        additional_charge = 50  # Extra charge for cars
        total = base_rent + additional_charge
        print(f"Car rental for {days} days: Rs.{base_rent} + Rs.{additional_charge} (AC charge) = Rs.{total}")
        return total

class Bike(Vehicle):
    def calculate_rent(self, days):
        base_rent = super().calculate_rent(days)
        discount = base_rent * 0.1  # 10% discount for bikes
        total = base_rent - discount
        print(f"Bike rental for {days} days: Rs.{base_rent} - Rs.{discount:.2f} (10% discount) = Rs.{total:.2f}")
        return total

class Scooter(Vehicle):
    def calculate_rent(self, days):
        base_rent = super().calculate_rent(days)
        print(f"Scooter rental for {days} days: Rs.{base_rent}")
        return base_rent

#vehicle objects
print("VEHICLE RENTAL SYSTEM\n")
car = Car("Honda", "Accord", 1000)
bike = Bike("Royal", "Enfield", 500)
scooter = Scooter("Vespa", "LX150", 250)

print("CAR RENTAL:")
car.display_info()
car.calculate_rent(5)

print("\nBIKE RENTAL:")
bike.display_info()
bike.calculate_rent(5)

print("\nSCOOTER RENTAL:")
scooter.display_info()
scooter.calculate_rent(5)