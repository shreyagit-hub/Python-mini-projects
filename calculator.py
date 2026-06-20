'''a calculator that can add different numbers of values using one method'''

class Calculator:
    def add(self, *numbers):
        """Add variable number of arguments"""
        if len(numbers) == 0:
            return 0
        total = sum(numbers)
        print(f"Sum of {numbers} = {total}")
        return total
    
    def multiply(self, *numbers):
        """Multiply variable number of arguments"""
        if len(numbers) == 0:
            return 0
        result = 1
        for num in numbers:
            result *= num
        print(f"Product of {numbers} = {result}")
        return result
    
    def subtract(self, first, *rest):
        """Subtract from first number"""
        if len(rest) == 0:
            return first
        result = first
        for num in rest:
            result -= num
        print(f"{first} - {' - '.join(map(str, rest))} = {result}")
        return result

# Create calculator and test
print("CALCULATOR METHOD OVERLOADING SIMULATION\n")
calc = Calculator()

print("1. Adding numbers:")
calc.add(5)
calc.add(5, 10)
calc.add(5, 10, 15)
calc.add(5, 10, 15, 20, 25)

print("\n2. Multiplying numbers:")
calc.multiply(3)
calc.multiply(3, 4)
calc.multiply(2, 3, 4)
calc.multiply(2, 3, 4, 5)

print("\n3. Subtracting numbers:")
calc.subtract(100, 25)
calc.subtract(100, 25, 15)
calc.subtract(100, 10, 20, 5)