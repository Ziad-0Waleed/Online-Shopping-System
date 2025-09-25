from datetime import datetime
from app.products.product import Product
from app.users.admin import Admin
from app.users.customer import Customer
from app.utils.auth import AuthUtils
from app.orders.payment import Payment


def print_header(title):
    print("\n" + "=" * 8 + " " + title + " " + "=" * 8)

def prompt_nonempty(prompt_text):
    while True:
        v = input(prompt_text).strip()
        if v:
            return v
        print("Value cannot be empty.")

def to_number(value):
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        s = value.strip().replace("$", "").replace(",", "")
        return float(s)
    raise TypeError("Unsupported total type")

class SimplePayment(Payment):
    def __init__(self, payment_id, order, method):
        super().__init__(payment_id, order, method)
        self._Payment__date = None
        self._Payment__status = None

    def process_payment(self):
        try:
            self._Payment__status = "Completed"
            self._Payment__date = datetime.now()
        except Exception:
            setattr(self, "status", "Completed")
            setattr(self, "date", datetime.now())
        return f"Payment {getattr(self, '_Payment__payment_id', 'N/A')} completed."


PRODUCTS = {}
COUPONS = {}
USER_OBJECTS = {}


def bootstrap_demo_data():
    p1 = Product("P001", "Laptop", 1200.00, 5)
    p2 = Product("P002", "Milk (1L)", 2.50, 20, expiry_date="2026-01-01")
    p3 = Product("P003", "Headphones", 80.00, 10)
    PRODUCTS[p1.product_id] = p1
    PRODUCTS[p2.product_id] = p2
    PRODUCTS[p3.product_id] = p3

    try:
        if "admin@example.com" not in AuthUtils.users_db:
            AuthUtils.register_user("admin@example.com", "admin pass", "Site Admin", "admin")
        if "ziad@example.com" not in AuthUtils.users_db:
            AuthUtils.register_user("ziad@example.com", "secret", "Ziad", "customer")
    except Exception:
        pass

    if "admin@example.com" not in USER_OBJECTS:
        USER_OBJECTS["admin@example.com"] = Admin("admin@example.com", "admin pass", "Site Admin")
    if "ziad@example.com" not in USER_OBJECTS:
        USER_OBJECTS["ziad@example.com"] = Customer("ziad@example.com", "secret", "Ziad")


def register_flow():
    print_header("Register new user")
    role = None
    while role not in ("admin", "customer"):
        role = input("Role (admin/customer): ").strip().lower()
        if role not in ("admin", "customer"):
            print("Please type 'admin' or 'customer'.")

    name = prompt_nonempty("Full name: ")
    email = prompt_nonempty("Email: ").lower()
    password = input("Password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    try:
        AuthUtils.register_user(email, password, name, role)
        print(f"Registered {role}: {email}")
    except Exception as e:
        print("Registration failed:", e)
        return

    if role == "admin":
        USER_OBJECTS[email] = Admin(email, password, name)
    else:
        USER_OBJECTS[email] = Customer(email, password, name)

def login_flow():
    print_header("Login")
    email = prompt_nonempty("Email: ").lower()
    password = input("Password: ").strip()

    try:
        res = AuthUtils.login(email, password)
    except Exception as e:
        print("Auth check raised exception:", e)
        return None

    ok = False

    if isinstance(res, bool):
        ok = res
    elif isinstance(res, str):
        ok = "success" in res.lower() or "ok" in res.lower()
    else:
        ok = bool(res)

    if not ok:
        print("Login failed. Check email/password.")
        return None


    role = None
    name = None
    entry = AuthUtils.users_db.get(email)
    if entry:
        role = entry.get("role")
        name = entry.get("name")

    user_obj = USER_OBJECTS.get(email)
    if user_obj is None:
        try:
            if role == "admin":
                user_obj = Admin(email, password, name or email)
            else:
                user_obj = Customer(email, password, name or email)
            USER_OBJECTS[email] = user_obj
        except Exception as e:
            print("Failed to create user object:", e)
            return None

    print(f"Login successful. Welcome, {getattr(user_obj, 'name', email)} ({role}).")
    return user_obj

def main_menu():
    bootstrap_demo_data()
    print_header("Online Shopping System (Interactive)")

    while True:
        print("\nMain Menu")
        print("1) Register")
        print("2) Login")
        print("3) Show product catalog")
        print("4) Exit")

        choice = input("Choose: ").strip()
        if choice == "1":
            register_flow()
        elif choice == "2":
            user = login_flow()
            if user is None:
                continue

            from app.users.admin import Admin as AdminClass
            if isinstance(user, AdminClass):
                try:
                    user.view_menu(PRODUCTS, COUPONS)
                except Exception as e:
                    print("Admin menu error:", e)
            else:
                try:
                    user.view_menu(PRODUCTS, COUPONS)
                except Exception as e:
                    print("Customer menu error:", e)

        elif choice == "3":
            print_header("Product Catalog")
            if not PRODUCTS:
                print("No products in catalog.")
            else:
                for pid, p in PRODUCTS.items():
                    print(p)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 1-4.")

if __name__ == "__main__":
    main_menu()
