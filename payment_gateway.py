'''a payment system that supports multiple payment methods'''

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def validate(self):
        pass

class CreditCardPayment(Payment):
    def __init__(self, amount, card_number, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.cvv = cvv
    
    def validate(self):
        if len(self.card_number) == 16 and len(self.cvv) == 3:
            return True
        return False
    
    def pay(self):
        if self.validate():
            print(f"Payment of Rs.{self.amount} processed via Credit Card")
            print(f"  Card: ****-****-****-{self.card_number[-4:]}")
            return True
        else:
            print("Invalid Credit Card Details!")
            return False

class MobileBankingPayment(Payment):
    def __init__(self, amount, phone_number, pin):
        super().__init__(amount)
        self.phone_number = phone_number
        self.pin = pin
    
    def validate(self):
        if len(self.phone_number) == 10 and len(self.pin) == 4:
            return True
        return False
    
    def pay(self):
        if self.validate():
            print(f"Payment of Rs.{self.amount} processed via Mobile Banking")
            print(f"  Phone: {self.phone_number}")
            return True
        else:
            print("Invalid Mobile Banking Details!")
            return False

class CashPayment(Payment):
    def __init__(self, amount, denominations=None):
        super().__init__(amount)
        self.denominations = denominations or []
    
    def validate(self):
        return True
    
    def pay(self):
        total_cash = sum(self.denominations)
        if total_cash >= self.amount:
            print(f"Payment of Rs.{self.amount} processed via Cash")
            change = total_cash - self.amount
            if change > 0:
                print(f"  Change: Rs.{change}")
            return True
        else:
            print("Insufficient cash provided!")
            return False

# Process payments
print("PAYMENT GATEWAY SYSTEM\n")

print("1. Credit Card Payment:")
cc_payment = CreditCardPayment(150, "1234567890123456", "123")
cc_payment.pay()

print("\n2. Mobile Banking Payment:")
mb_payment = MobileBankingPayment(200, "9876543210", "5678")
mb_payment.pay()

print("\n3. Cash Payment:")
cash_payment = CashPayment(100, [50, 50, 20])
cash_payment.pay()

print("\n4. Invalid Credit Card:")
invalid_cc = CreditCardPayment(100, "1234", "12")
invalid_cc.pay()