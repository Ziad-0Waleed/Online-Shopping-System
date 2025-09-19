from base_user import User

class Admin(User):
    def __init__(self, email, password, name):

        super().__init__(email, password, name)
        self.role = "admin"
        
    def add_product(self,product):
        pass

    def remove_product(self,product_id):
        pass

    def update_product_price(self,product_id,new_price):
        pass

    def apply_discount(self,product_id,discount):
        pass

    def remove_discount(self,product_id):
        pass

    def check_stock(self,product_id):
        pass

    def view_menu(self):
        print(  "1. Add new product",
                "\n2. Remove product",
                "\n3. Modify product price",
                "\n4. Add discounts",
                "\n5. Remove discounts",
                "\n6. Check stock levels")
        


