from datetime import datetime
from payment import Payment

class CreditCard(Payment):
    def __init__(self, payment_id, order,method, card_number, expiration, cvv):
        super().__init__(payment_id, order, method)

        self._Payment__date = None
        self._Payment__status = None
        self.__card_number = str(card_number)
        self.__expiration = (datetime.strptime(expiration, "%Y-%m").date()
                             if expiration else None
                             )
        self.__cvv = str(cvv)

    def _validate_card(self):
        if not self.__card_number.isdigit() or not len(self.__card_number) == 16:
            raise ValueError("Card number must be 16 digits")

        if not self.__cvv.isdigit() or len(self.__cvv) not in (3, 4):
            raise ValueError("CVV must be 3 or 4 digits")

        try:
            parts = self.__expiration.split("/")
            if len(parts) != 2:
                raise ValueError
            month = int(parts[0])
            year = int(parts[1])
            if year < 100:  # "24" -> 2024
                year += 2000
            if not 1 <= month <= 12:
                raise ValueError
            exp_date = datetime(year, month, 1)
            now = datetime.now()
            if (year < now.year) or (year == now.year and month < now.month):
                raise ValueError("Card expired")
        except ValueError:
            raise ValueError("Expiration must be in MM/YY format and not expired")

    def process_payment(self):
        self._Payment__status = "Completed"
        self._Payment__date = datetime.now()
        return f"Card payment of {self.amount} completed."


