# Example 2: Payment Processing
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


# Using the subclasses
credit = CreditCardPayment()
paypal = PayPalPayment()

credit.process_payment(100)
paypal.process_payment(150)
