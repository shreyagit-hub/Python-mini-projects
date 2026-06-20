'''a ride-sharing fare calculator like a taxi or ride-booking app'''

class Ride:
    def __init__(self, distance, base_fare):
        self.distance = distance
        self.base_fare = base_fare
    
    def calculate_fare(self):
        fare = self.base_fare + (self.distance * 2)
        print(f"Distance: {self.distance} km | Base Fare: Rs.{self.base_fare} | Total: Rs.{fare}")
        return fare

class BikeRide(Ride):
    def calculate_fare(self):
        base_calculation = self.base_fare + (self.distance * 2)
        discount = base_calculation * 0.15  # 15% discount
        fare = base_calculation - discount
        print(f"Bike Ride - Distance: {self.distance} km | Fare: Rs.{base_calculation} - Rs.{discount:.2f} (15% discount) = Rs.{fare:.2f}")
        return fare

class CarRide(Ride):
    def calculate_fare(self):
        base_calculation = self.base_fare + (self.distance * 2)
        surge_charge = 5
        fare = base_calculation + surge_charge
        print(f"Car Ride - Distance: {self.distance} km | Fare: Rs.{base_calculation} + Rs.{surge_charge} (surge) = Rs.{fare:.2f}")
        return fare

class PremiumRide(Ride):
    def calculate_fare(self):
        base_calculation = self.base_fare + (self.distance * 2)
        premium_charge = base_calculation * 0.25  # 25% premium
        fare = base_calculation + premium_charge
        print(f"Premium Ride - Distance: {self.distance} km | Fare: Rs.{base_calculation} + Rs.{premium_charge:.2f} (25% premium) = Rs.{fare:.2f}")
        return fare

# Calculate fares
print("RIDE SHARING FARE CALCULATOR\n")
distance = 10
base_fare = 50

print("1. Bike Ride:")
bike = BikeRide(distance, base_fare)
bike.calculate_fare()

print("\n2. Car Ride:")
car = CarRide(distance, base_fare)
car.calculate_fare()

print("\n3. Premium Ride:")
premium = PremiumRide(distance, base_fare)
premium.calculate_fare()

print("Comparing different ride types for same distance:")
rides = [
    BikeRide(distance, base_fare),
    CarRide(distance, base_fare),
    PremiumRide(distance, base_fare)
]

for ride in rides:
    ride.calculate_fare()