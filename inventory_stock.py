'''a stock management system for a small shop'''

class Product:
    def __init__(self, product_name, price, stock_quantity):
        self.product_name = product_name
        self.price = price
        self.__stock_quantity = stock_quantity
    
    def get_stock(self):
        return self.__stock_quantity
    
    def set_stock(self, quantity):
        if quantity < 0:
            print("Stock quantity cannot be negative!")
            return False
        else:
            self.__stock_quantity = quantity
            print(f"Stock updated to {self.__stock_quantity}")
            return True
    
    def add_stock(self, quantity):
        if quantity < 0:
            print("Cannot add negative quantity!")
            return False
        self.__stock_quantity += quantity
        print(f"Stock updated to {self.__stock_quantity}")
        return True
    
    def remove_stock(self, quantity):
        if quantity < 0:
            print("Cannot remove negative quantity!")
            return False
        if quantity > self.__stock_quantity:
            print(f"Insufficient stock! Available: {self.__stock_quantity}")
            return False
        self.__stock_quantity -= quantity
        print(f"Stock updated to {self.__stock_quantity}")
        return True
    
    def display_info(self):
        print(f"Product: {self.product_name}")
        print(f"Price: Rs.{self.price}")
        print(f"Stock: {self.__stock_quantity} units")
        print("-" * 40)

# Create and manage inventory
print("INVENTORY STOCK MANAGEMENT SYSTEM\n")
product1 = Product("Laptop", 100000, 50)
product2 = Product("Mouse", 1200, 200)
product3 = Product("Keyboard", 3000, 100)

print("1. Initial Inventory:")
product1.display_info()
product2.display_info()
product3.display_info()

print("2. Adding Stock:")
product1.add_stock(20)
product2.add_stock(50)

print("\n3. Removing Stock:")
product1.remove_stock(10)
product2.remove_stock(30)
product3.remove_stock(150)  # Should fail

print("\n4. Invalid Operations:")
product1.set_stock(-5)
product1.add_stock(-10)

print("\n5. Final Inventory:")
product1.display_info()
product2.display_info()
product3.display_info()