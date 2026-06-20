'''a system that allows customers to order food from a restaurant menu'''

class FoodItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def display_info(self):
        print(f"{self.name} - ${self.price} ({self.category})")

class Order:
    def __init__(self):
        self.items = []
    
    def add_food(self, food_item, quantity=1):
        self.items.append({"food": food_item, "quantity": quantity})
        print(f"Added {quantity}x {food_item.name} to order")
    
    def calculate_bill(self):
        total = sum(item["food"].price * item["quantity"] for item in self.items)
        return total
    
    def print_order_summary(self):
        if not self.items:
            print("Order is empty!")
            return
        
        print("\n-----ORDER SUMMARY-----\n")
        print("-" * 50)
        for item in self.items:
            food = item["food"]
            qty = item["quantity"]
            subtotal = food.price * qty
            print(f"{food.name} x {qty} | Rs.{food.price} each | Rs.{subtotal}")
        print("-" * 50)
        print(f"Total Bill: Rs.{self.calculate_bill()}")
        print("-" * 50 + "\n")

# Create food items and order
print("RESTAURANT FOOD ORDERING SYSTEM\n")
item1 = FoodItem("Burger", 180, "Main Course")
item2 = FoodItem("Fries", 100, "Sides")
item3 = FoodItem("Coke", 50, "Beverage")
item4 = FoodItem("Ice Cream", 120, "Dessert")

order = Order()
order.add_food(item1, 2)
order.add_food(item2, 1)
order.add_food(item3, 2)
order.add_food(item4, 1)

order.print_order_summary()