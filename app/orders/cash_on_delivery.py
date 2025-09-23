from datetime import datetime
from payment import Payment


class CashOnDelivery(Payment):
    def __init__(self, payment_id, order, extra_cod_fees = 30):
        super().__init__(payment_id, order, "Cash On Delivery (COD)")

        self._Payment__date = None
        self._Payment__status = None
        self._extra_cod_fees = extra_cod_fees

    def process_payment(self):
        self._Payment__status = "To Be Charged"
        self._Payment__date = datetime.today()
        return f"Order Confirmed (COD) Please Make Sure You Have {self.amount}"
