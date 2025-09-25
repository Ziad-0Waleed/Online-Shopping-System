import time
from app.users.base_user import User
from app.products.coupon import Coupon

class Admin(User):
    def __init__(self, email, password, name):

        super().__init__(email, password, name)
        self.role = "admin"

    @staticmethod
    def add_product(products,product):
        if product is None:
            raise ValueError("Product must be provided")
        pid = product.product_id
        if pid in products:
            raise ValueError(f"Product {pid} already exists")
        products[pid] = product
        return product

    @staticmethod
    def remove_product(products,product_id):
        if product_id is None:
            raise ValueError("Product ID must be provided")
        if product_id not in products:
            raise ValueError(f"Product {product_id} not found")
        return products.pop(product_id)

    @staticmethod
    def update_product_price(products,product_id,new_price):
        if product_id not in products:
            raise ValueError(f"Product {product_id} not found")
        product = products[product_id]
        if new_price < 0:
            raise ValueError("Price must be positive")
        product.price = float(new_price)
        return product.price

    @staticmethod
    def apply_discount(coupons, product_id, discount_percentage, expiry_date=None, coupon_code=None):
        if not (0 <= float(discount_percentage) <= 100):
            raise ValueError("discount_percentage must be between 0 and 100")

        if coupon_code is None:
            coupon_code = f"DISC-{product_id}-{int(time.time())}"

        coupon = Coupon(code=coupon_code,
                        discount_percentage=float(discount_percentage),
                        expiry_date=expiry_date,
                        applicable_products=[product_id])

        coupons[coupon_code] = coupon
        return coupon

    @staticmethod
    def remove_discount(coupons, coupon_code=None, product_id=None):
        if coupon_code:
            if coupon_code not in coupons:
                raise KeyError(f"Coupon {coupon_code} not found")
            return coupons.pop(coupon_code)

        if product_id:
            removed = []
            for code, c in list(coupons.items()):
                try:
                    applies = c.applies_to(product_id)
                except Exception:
                    applies = False
                if applies:
                    removed.append(coupons.pop(code))
            return removed

        raise ValueError("Either coupon_code or product_id must be provided")

    @staticmethod
    def check_stock(products: dict, product_id):
        if product_id not in products:
            raise KeyError(f"Product {product_id} not found")
        return products[product_id].stock

    def view_menu(self, products, coupons = None):
        if coupons is None:
            coupons = {}

        while True:
            print("\n--- Admin Menu ---")
            print("1. Add new product")
            print("2. Remove product")
            print("3. Modify product price")
            print("4. Add discount (coupon)")
            print("5. Remove discount")
            print("6. Check stock levels")
            print("7. List products")
            print("8. Exit")
            try:
                choice = int(input("Choose: ").strip())
            except ValueError:
                print("Invalid input")
                continue

            if choice == 1:
                # Add new product with optional expiry
                pid = input("Product id: ").strip()
                name = input("Name: ").strip()

                # price validation loop
                while True:
                    price_raw = input("Price: ").strip()
                    try:
                        price = float(price_raw)
                        if price <= 0:
                            raise ValueError("Price must be positive")
                        break
                    except Exception as e:
                        print("Invalid price. Enter a positive number.")

                # stock validation loop
                while True:
                    stock_raw = input("Stock: ").strip()
                    try:
                        stock = int(stock_raw)
                        if stock < 0:
                            raise ValueError("Stock cannot be negative")
                        break
                    except Exception:
                        print("Invalid stock. Enter a non-negative integer.")

                # expiry date optional; accept blank for None, otherwise validate YYYY-MM-DD
                while True:
                    expiry_in = input("Expiry date (YYYY-MM-DD) or leave blank for no expiry: ").strip()
                    if expiry_in == "":
                        expiry_val = None
                        break
                    # validate format
                    from datetime import datetime
                    try:
                        # this will raise if format is wrong
                        datetime.strptime(expiry_in, "%Y-%m-%d")
                        expiry_val = expiry_in  # keep string; Product constructor will parse
                        break
                    except ValueError:
                        print("Invalid date format. Use YYYY-MM-DD or leave blank.")


                from app.products.product import Product
                p = Product(pid, name, price, stock, expiry_date=expiry_val)
                try:
                    self.add_product(products, p)
                    print("Product added:", p)
                except Exception as e:
                    print("Failed to add product:", e)

            elif choice == 2:
                pid = input("Product id to remove: ").strip()
                try:
                    removed = self.remove_product(products, pid)
                    print("Removed:", removed)
                except Exception as e:
                    print("Failed to remove:", e)

            elif choice == 3:
                pid = input("Product id: ").strip()
                try:
                    new_price = float(input("New price: ").strip())
                    updated = self.update_product_price(products, pid, new_price)
                    print(f"Updated price for {pid} to {updated}")
                except Exception as e:
                    print("Failed to update price:", e)

            elif choice == 4:
                pid = input("Product id to discount: ").strip()
                pct = float(input("Discount % (e.g. 10 for 10%): ").strip())
                expiry = input("Expiry (YYYY-MM-DD) or blank: ").strip() or None
                try:
                    coupon = self.apply_discount(coupons, pid, pct, expiry)
                    print("Created coupon:", coupon)
                except Exception as e:
                    print("Failed to create coupon:", e)

            elif choice == 5:
                code = input("Coupon code to remove (leave blank to remove by product): ").strip()
                try:
                    if code:
                        self.remove_discount(coupons, coupon_code=code)
                        print("Removed coupon", code)
                    else:
                        pid = input("Product id to remove discounts for: ").strip()
                        removed = self.remove_discount(coupons, product_id=pid)
                        print("Removed coupons:", removed)
                except Exception as e:
                    print("Failed to remove coupon(s):", e)

            elif choice == 6:
                pid = input("Product id to check stock: ").strip()
                try:
                    stock = self.check_stock(products, pid)
                    print(f"{pid} stock: {stock}")
                except Exception as e:
                    print("Error:", e)

            elif choice == 7:
                print("--- Products ---")
                for pid, p in products.items():
                    print(p)
            elif choice == 8:
                break
            else:
                print("Unknown option")
        


