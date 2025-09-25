from app.users.base_user import User
from app.cart.cart import Cart
from app.orders.order import Order
from app.products.coupon import Coupon
from datetime import datetime

class Customer(User):
    def __init__(self, email,password ,name ):
        super().__init__(email, password, name)
        self.role = "customer"
        self.cart = Cart()
        self.orders = []
        self.address = None
        self.payment_info = None
        self.active_coupon = None

    @staticmethod
    def view_products(products):
        print("\n--- Available Products ---")
        if not products:
            print("No products available.")
            return
        for pid, product in products.items():
            print(f"{pid} → {product.name} (${product.price:.2f}) | Stock: {product.stock}")

    def add_to_cart(self,product,quantity):
        if product is None:
            raise ValueError("Product must be provided")
        else:
            self.cart.add_item(product,quantity)
        print(f"Added {quantity} x {product.name} to cart.")

    def remove_from_cart(self,product):
        if product is None:
            raise ValueError("Product must be provided")
        else:
            self.cart.remove_item(product)
        print(f"Removed {product.name} from cart.")

    def remove_from_cart_by_id(self, product_id):
        item = self.cart.items.get(product_id)
        if not item:
            raise ValueError("Product not in cart")
        product = item["product"]
        self.remove_from_cart(product)

    def view_cart(self):
        print("--- Your Cart ---")
        self.cart.list_items()

    def apply_coupon(self,coupon):
        if coupon is None:
            print("No coupon provided.")
            return
        if not isinstance(coupon, Coupon):
            raise TypeError("coupon must be a Coupon instance")
        if not coupon.is_valid():
            print("Coupon is expired or invalid.")
            return
        self.cart.apply_coupon(coupon)
        self.active_coupon = coupon
        print(f"Coupon {coupon.code} applied to cart.")

    def checkout(self, payment_method, address):
        if self.cart.is_empty():
            print("Your cart is empty.")
            return None

        order_id = f"ORD{int(datetime.now().timestamp())}"

        order = Order(
            order_id=order_id,
            customer=self.name,
            cart=self.cart,
            payment_method=payment_method,
            address=address,
        )

        try:
            order.confirm_order()
        except Exception as exc:
            print("Failed to confirm order:", exc)
            return None

        self.orders.append(order)
        self.cart = Cart()  # empty cart after successful order
        self.active_coupon = None
        print(f"Order {order_id} placed successfully. Total: {order.total}")
        return order


    def view_menu(self, products: dict, coupons: dict = None):
        if coupons is None:
            coupons = {}

        while True:
            print("\n--- Customer Menu ---")
            print("1. View products")
            print("2. Add to cart")
            print("3. View cart")
            print("4. Remove from cart")
            print("5. Apply coupon")
            print("6. Checkout")
            print("7. View orders")
            print("8. Exit")
            try:
                choice = int(input("Enter choice: ").strip())
            except ValueError:
                print("Invalid input.")
                continue

            if choice == 1:
                self.view_products(products)

            elif choice == 2:
                pid = input("Product ID: ").strip()
                if pid not in products:
                    print("Product not found.")
                    continue
                try:
                    qty = int(input("Quantity: ").strip())
                except ValueError:
                    print("Quantity must be integer.")
                    continue
                try:
                    self.add_to_cart(products[pid], qty)
                except Exception as e:
                    print("Failed to add to cart:", e)

            elif choice == 3:
                self.view_cart()

            elif choice == 4:
                pid = input("Product ID to remove: ").strip()
                try:
                    self.remove_from_cart_by_id(pid)
                except Exception as e:
                    print("Remove failed:", e)

            elif choice == 5:
                code = input("Coupon code: ").strip()
                coupon = coupons.get(code)
                if not coupon:
                    print("Coupon not found.")
                    continue
                try:
                    self.apply_coupon(coupon)
                except Exception as e:
                    print("Failed to apply coupon:", e)

            elif choice == 6:
                print("Payment methods: 1) Cash On Delivery (COD)  2) Credit/Debit Card")
                pm = input("Choose (1/2): ").strip()
                if pm == "1":
                    payment_method = "Cash On Delivery (COD)"
                else:
                    payment_method = "Credit/Debit Card"
                address = input("Shipping address: ").strip()
                order = self.checkout(payment_method, address)
                if order:
                    print("\n" + order.generate_receipt())

            elif choice == 7:
                if not self.orders:
                    print("No orders yet.")
                for o in self.orders:
                    print("\n" + o.generate_receipt())

            elif choice == 8:
                print("Exiting customer menu.")
                break

            else:
                print("Invalid choice.")



