'''a shopping cart system similar to real e-commerce websites'''

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total_price(self):
        return self.price * self.quantity

class Cart:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.quantity} x {product.name} to cart")
    
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Removed {product_name} from cart")
                return
        print(f"{product_name} not found in cart")
    
    def calculate_total(self):
        total = sum(product.get_total_price() for product in self.products)
        return total
    
    def display_cart(self):
        if not self.products:
            print("Cart is empty!")
            return
        
        print("\n" + "=" * 60)
        print("SHOPPING CART")
        print("=" * 60)
        for product in self.products:
            print(f"{product.name} | Qty: {product.quantity} | Price: ${product.price} | Total: ${product.get_total_price()}")
        print("-" * 60)
        print(f"Cart Total: ${self.calculate_total()}")
        print("=" * 60 + "\n")

#create products and cart
print("ONLINE SHOPPING CART SYSTEM\n")
product1 = Product("Laptop", 999.99, 1)
product2 = Product("Mouse", 29.99, 2)
product3 = Product("Keyboard", 79.99, 1)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.display_cart()

cart.remove_product("Mouse")
cart.display_cart()