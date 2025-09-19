from cart import Cart

class Order:
    def __init__(self, order_id, customer, cart, payment_method, address, status="Pending"):
        self.__order_id = order_id
        self.__customer = customer
        self.__cart = cart               # Cart object, not raw items
        self.__total = cart.calculate_total()
        self.__payment_method = payment_method
        self.__address = address
        self.__status = status         

    @property
    def order_id(self):
        return self.__order_id

    @property
    def total(self):
        return self.__total

    @property
    def status(self):
        return self.__status  

    def confirm_order(self):
        pass

    def cancel_order(self):
        pass

    def update_status(self, new_status):
        pass

    def generate_receipt(self):
        pass
