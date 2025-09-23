class Order:
    def __init__(self, order_id, customer, cart, payment_method, address, status="Pending"):
        self.__order_id = order_id
        self.__customer = customer
        self.__cart = cart
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
        if not self.__cart.items:
            raise ValueError("Cart is empty")
        for _,data in self.__cart.items.items():
            product = data["product"]
            quantity = data["quantity"]
            product.reduce_stock(quantity)
        self.__status = "Confirmed"

    def cancel_order(self):
        if self.__status == "Cancelled":
            raise ValueError("Order is already cancelled")

        if self.__status == "Confirmed":
            for _,data in self.__cart.items.items():
                product = data["product"]
                quantity = data["quantity"]
                product.add_stock(quantity)
        self.__status = "Cancelled"

    def update_status(self, new_status):
        valid_statuses = ["Pending", "Confirmed", "Shipped", "Delivered", "Cancelled"]

        if new_status not in valid_statuses:
            raise ValueError("Invalid Status")

        self.__status = new_status

    def generate_receipt(self):
        lines = [f"Order No.: {self.__order_id}", f"Customer: {self.__customer}",f"Address: {self.__address}", f"Items:"]
        sub_total = 0.0
        for _,data in self.__cart.items.items():
            product = data["product"]
            quantity = data["quantity"]
            line_total = product.price * quantity
            sub_total += line_total
            lines.append(f"  - {product.name} x {quantity} = ${line_total:.2f}")
        lines.append(f"Subtotal: {sub_total}")
        lines.append("-----------------------------")
        lines.append(f"Total: {self.__total}")
        lines.append(f"Payment Method: {self.__payment_method}")
        lines.append(f"Status: {self.__status}")
        return "\n".join(lines)