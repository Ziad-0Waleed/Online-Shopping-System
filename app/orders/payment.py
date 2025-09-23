from abc import ABC,abstractmethod
from datetime import datetime

class Payment(ABC):
    def __init__(self, payment_id, order, method):
        self.__payment_id = payment_id
        self.__order = order
        self.__amount = order.total
        self.__method = self.validate_method(method)
        self.__status = "Pending"
        self.__date = None

    @property
    def status(self):
        return self.__status

    @property
    def amount(self):
        return self.__amount

    @property
    def method(self):
        return self.__method

    @staticmethod
    def validate_method(method):
        valid_methods = ["Cash On Delivery (COD)", "Credit/Debit Card"]
        if method not in valid_methods:
            raise ValueError("Invalid payment method")
        return method
    
    @abstractmethod
    def process_payment(self):
        
        pass

    def refund(self):
        if self.__status != "Confirmed":
            raise ValueError("Cannot refund payment that has not been confirmed")
        self.__status = "Refunded"
        self.__date = datetime.now()
        return f"Payment {self.__payment_id} refunded successfully"

