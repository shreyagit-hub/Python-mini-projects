'''a notification system that sends messages through different platforms'''

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, recipient, subject, message):
        self.recipient = recipient
        self.subject = subject
        self.message = message
    
    @abstractmethod
    def send(self):
        pass
    
    @abstractmethod
    def format_message(self):
        pass

class EmailNotification(Notification):
    def __init__(self, recipient, subject, message):
        super().__init__(recipient, subject, message)
        self.email = recipient
    
    def format_message(self):
        return f"Subject: {self.subject}\n\n{self.message}"
    
    def send(self):
        formatted = self.format_message()
        print("-----EMAIL NOTIFICATION-----\n")
        print(f"To: {self.email}")
        print(formatted)
        print("-" * 50 + "\n")

class SMSNotification(Notification):
    def __init__(self, recipient, subject, message):
        super().__init__(recipient, subject, message)
        self.phone = recipient
    
    def format_message(self):
        # SMS has character limit
        return self.message[:160]
    
    def send(self):
        formatted = self.format_message()
        print("-----SMS NOTIFICATION-----\n")
        print(f"To: {self.phone}")
        print(f"Message: {formatted}")
        print("-" * 50 + "\n")

class WhatsAppNotification(Notification):
    def __init__(self, recipient, subject, message):
        super().__init__(recipient, subject, message)
        self.phone = recipient
    
    def format_message(self):
        return f"📱 {self.subject}\n\n{self.message}"
    
    def send(self):
        formatted = self.format_message()
        print("-----WHATSAPP NOTIFICATION-----\n")
        print(f"To: {self.phone}")
        print(formatted)
        print("-" * 50 + "\n")

#send notifications
print("NOTIFICATION SENDING SYSTEM\n")
email = EmailNotification(
    "user@example.com",
    "Welcome to Our Service",
    "Hello! Welcome to our platform. We're glad to have you on board."
)
email.send()

sms = SMSNotification(
    "555-1234",
    "Verification Code",
    "Your verification code is 123456. Do not share this code with anyone."
)
sms.send()

whatsapp = WhatsAppNotification(
    "555-5678",
    "Order Confirmation",
    "Your order has been confirmed! Order ID: ORD123. Delivery in 2-3 days."
)
whatsapp.send()