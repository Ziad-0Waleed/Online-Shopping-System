# from app.products.product import Product
# from app.products.coupon import Coupon
# from app.cart.cart import Cart

# def main():
#     # --- Create Products ---
#     p1 = Product("P001", "Laptop", 1200.0, 5)
#     p2 = Product("P002", "Mouse", 25.0, 50)
#     p3 = Product("P003", "Keyboard", 45.0, 30, expiry_date="2026-12-31")

#     print("Created Products:")
#     print(p1)
#     print(p2)
#     print(p3)
#     print("-" * 40)

#     # --- Create Coupons ---
#     c1 = Coupon("SAVE10", 10, expiry_date="2030-01-01")   # valid coupon, 10% off everything
#     c2 = Coupon("MOUSE20", 20, expiry_date="2030-01-01", applicable_products=["P002"]) # 20% off mouse
#     c3 = Coupon("EXPIRED", 50, expiry_date="2000-01-01")  # expired coupon

#     print("Created Coupons:")
#     print(c1)
#     print(c2)
#     print(c3)
#     print("-" * 40)

#     # --- Create Cart & Add Items ---
#     cart = Cart()
#     cart.add_item(p1, 1)
#     cart.add_item(p2, 2)
#     cart.add_item(p3, 3)

#     print("Cart Items after adding:")
#     cart.list_items()
#     print(f"Total without coupon: ${cart.calculate_total():.2f}")
#     print("-" * 40)

#     # --- Apply Valid Coupon ---
#     print("Applying SAVE10 coupon...")
#     cart.apply_coupon(c1)
#     print(f"Total with SAVE10: ${cart.calculate_total():.2f}")
#     print("-" * 40)

#     # --- Apply Product-specific Coupon ---
#     print("Applying MOUSE20 coupon...")
#     cart.apply_coupon(c2)
#     print(f"Total with MOUSE20: ${cart.calculate_total():.2f}")
#     print("-" * 40)

#     # --- Try Expired Coupon ---
#     print("Trying expired coupon...")
#     try:
#         cart.apply_coupon(c3)
#     except ValueError as e:
#         print(f"Error: {e}")
#     print("-" * 40)

#     # --- Update Quantity ---
#     print("Updating Laptop quantity to 2...")
#     cart.update_quantity(p1, 2)
#     cart.list_items()
#     print(f"Total after update (MOUSE20 coupon still applied): ${cart.calculate_total():.2f}")
#     print("-" * 40)

#     # --- Remove Item ---
#     print("Removing Mouse from cart...")
#     cart.remove_item(p2)
#     cart.list_items()
#     print(f"Final total: ${cart.calculate_total():.2f}")
#     print("-" * 40)

# if __name__ == "__main__":
#     main()
