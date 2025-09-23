from datetime import datetime
from payment import Payment

class CreditCard(Payment):
    def __init__(self, payment_id, order, card_number, expiration, cvv):
        super().__init__(payment_id, order, "Credit/Debit Card")

        self._Payment__date = None
        self._Payment__status = None
        self.__card_number = card_number
        self.__expiration = expiration
        self.__cvv = cvv

    def process_payment(self):
        self._Payment__status = "Completed"
        self._Payment__date = datetime.now()
        return f"Card payment of {self.amount} completed."


