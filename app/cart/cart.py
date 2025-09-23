class Cart:
    def __init__(self):
        self.__items = {}
        self.__coupon = None

    def add_item(self,product,quantity=1):
        """Add a product with given quantity to the cart."""
        self.__items[product.product_id] = {"product": product,"quantity": quantity}

    def remove_item(self,product):
        """Remove a product from the cart."""
        if product.product_id in self.__items:
            self.__items.pop(product.product_id)
        else:
            raise ValueError(f"Product {product.product_id} not in cart")

    def update_quantity(self,product,quantity):
        """Update the quantity of a product by the product ID."""
        if product.product_id not in self.__items:
            raise ValueError("Product not found in cart")

        if quantity > product.stock:
            raise ValueError(f"Product {product.product_id} quantity exceeds quantity limit")

        self.__items[product.product_id]["quantity"] = quantity


    def apply_coupon(self, coupon):
        if coupon is None:
            self.__coupon = None
            return
        if not coupon.is_valid():
            raise ValueError("Coupon is expired or invalid")
        self.__coupon = coupon   


    def calculate_total(self):
        total = 0.0
        for product_id,data in self.__items.items():
            product = data["product"]
            quantity = data["quantity"]
            line_total = product.price * quantity

            if self.__coupon and self.__coupon.applies_to(product.product_id):
                discount = self.__coupon.discount_amount(line_total)
                total += line_total - discount
            else:
                total += line_total
        return f"${total}"


    def list_items(self):
        for product_id,data in self.__items.items():
            product = data["product"]
            quantity = data["quantity"]
            print(f"{product.name}: ${product.price} \n(ID: {product.product_id}) → {quantity} pcs ")

    @property
    def items(self):
        """Safe access to cart items"""
        return self.__items.copy()