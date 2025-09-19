from abc import ABC,abstractmethod
from datetime import datetime

class Payment(ABC):
    def __init__(self, payment_id, order, method):
        self.__payment_id = payment_id
        self.__order = order
        self.__amount = order.total
        self.__method = method
        self.__status = "Pending"
        self.__date = None

    @property
    def status(self):
        pass

    @property
    def amount(self):
        pass

    @staticmethod
    def validate_method(method):
        pass
    
    @abstractmethod
    def process_payment(self):
        
        pass

    def refund(self):
        
        pass

