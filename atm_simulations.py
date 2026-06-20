'''a simple ATM system where users can check balance, deposit, and withdraw money'''

class ATM:
    def __init__(self, pin, initial_balance=1000):
        self.__pin = pin
        self.__balance = initial_balance
        self.__is_authenticated = False
    
    def verify_pin(self, entered_pin):
        if entered_pin == self.__pin:
            self.__is_authenticated = True
            print("PIN verified successfully!")
            return True
        else:
            print("Invalid PIN!")
            return False
    
    def check_balance(self):
        if not self.__is_authenticated:
            print("Please verify PIN first!")
            return
        print(f"Current Balance: Rs.{self.__balance}")
    
    def deposit(self, amount):
        if not self.__is_authenticated:
            print("Please verify PIN first!")
            return
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs.{amount}. New Balance: Rs.{self.__balance}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if not self.__is_authenticated:
            print("Please verify PIN first!")
            return
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn: Rs.{amount}. New Balance: Rs.{self.__balance}")
            else:
                print(f"Insufficient balance! Available: Rs.{self.__balance}")
        else:
            print("Withdrawal amount must be positive!")
    
    def logout(self):
        self.__is_authenticated = False
        print("Logged out successfully!")

# ATM simulation
print("ATM MACHINE SIMULATION\n")
atm = ATM("1234", 5000)

print("1. Attempting to check balance without authentication:")
atm.check_balance()

print("\n2. Verifying PIN:")
atm.verify_pin("0000")  #wrong PIN example
atm.verify_pin("1234")  #correct PIN example

print("\n3. Checking balance:")
atm.check_balance()

print("\n4. Depositing money:")
atm.deposit(1000)

print("\n5. Withdrawing money:")
atm.withdraw(2000)
atm.withdraw(10000)  #insufficient balance example

print("\n6. Final balance:")
atm.check_balance()

print("\n7. Logging out:")
atm.logout()
atm.check_balance()