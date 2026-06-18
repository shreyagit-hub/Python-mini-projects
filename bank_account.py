'''a bank account system where the account balance cannot be accessed directly'''

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.__account_holder = account_holder
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: Rs.{amount}. New balance: Rs.{self.__balance}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn: Rs.{amount}. New balance: Rs.{self.__balance}")
            else:
                print(f"Insufficient balance! Current balance: Rs.{self.__balance}")
        else:
            print("Withdrawal amount must be positive!")
    
    def get_balance(self):
        return self.__balance
    
    def display_details(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: Rs.{self.__balance}")

#create bank accounts
print("BANK ACCOUNT SYSTEM\n")
account1 = BankAccount("John Doe", 10000)
account2 = BankAccount("Jane Smith", 5000)

account1.display_details()
print()

account1.deposit(50000)
account1.withdraw(2000)
account1.withdraw(20000)
print()

account2.display_details()
print()

account2.deposit(10000)
account2.withdraw(12000)
print(f"Current balance: Rs.{account2.get_balance()}")