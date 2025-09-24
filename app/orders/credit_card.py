from datetime import datetime
from payment import Payment

class CreditCard(Payment):
    def __init__(self, payment_id, order, card_number, expiration, cvv):
        super().__init__(payment_id, order, "Credit/Debit Card")

        self._Payment__date = None
        self._Payment__status = None
        self.__card_number = card_number
        self.__expiration = (datetime.strptime(expiration, "%Y-%m").date()
                             if expiration else None
                             )
        self.__cvv = cvv

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, value):
        if value < 16:
            raise ValueError("Invalid card number")
        self.__card_number = value

    @property
    def expiration(self):
        return self.__expiration

    @expiration.setter
    def expiration(self, value):
        if datetime.strptime(value, "%Y-%m").date() < self.__expiration:
            raise ValueError("Expired card")
        self.__expiration = value

    @property
    def cvv(self):
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        if 3 > value > 4:
            raise ValueError("Invalid cvv")
        self.__cvv = value

    def process_payment(self):
        self._Payment__status = "Completed"
        self._Payment__date = datetime.now()
        return f"Card payment of {self.amount} completed."


