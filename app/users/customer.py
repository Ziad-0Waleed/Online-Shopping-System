from base_user import User
from cart import Cart

class Customer(User):
    def __init__(self, email, password, name):

        super().__init__(email, password, name)
        self.role = "customer"
        self.cart = Cart()
        self.address = None
        self.payment_info = None

    def view_products(self):
        pass

    def add_to_cart(self,product_id,quantity):
        pass

    def remove_from_cart(self,product_id):
        pass

    def view_cart(self):
        pass

    def apply_coupon(self,code):
        pass

    def checkout(self,payment_method,address):
        pass

    def view_menu(self):
        print(  "1. View products",
                "\n2. Add to cart",
                "\n3. View cart",
                "\n4. Apply coupon",
                "\n5. Checkout")