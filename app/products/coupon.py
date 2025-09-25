from datetime import datetime
class Coupon:
    def __init__(self, code, discount_percentage, expiry_date=None, applicable_products=None):
        """
        :param code: unique string for coupon (e.g., "SAVE10")
        :param discount_percentage: integer/float like 10 for 10%
        :param expiry_date: date when coupon expires (optional)
        :param applicable_products: list of product IDs this coupon applies to (None means all)
        """
        self.__code = code
        self.__discount_percentage = discount_percentage
        self.__expiry_date =(
            datetime.strptime(expiry_date , "%Y-%m-%d").date()
            if expiry_date else None
        )
        self.__applicable_products = applicable_products or []

    @property
    def code(self):
        return self.__code

    @property
    def discount_percentage(self):
        return self.__discount_percentage

    @property
    def expiry_date(self):
        return self.__expiry_date

    @property
    def applicable_products(self):
        return self.__applicable_products

    def is_valid(self):
        """Return True if coupon is not expired. None expiry => no expiry (valid)."""
        if self.__expiry_date is None:
            return True
        return self.__expiry_date >= datetime.today().date()
        
    def applies_to(self, product_id):
        """Check if this coupon applies to a specific product."""
        if not self.__applicable_products:
            return True
        return product_id in self.__applicable_products
            

    def discount_amount(self, amount):
        """Return the discounted price after applying coupon."""
        if amount is None:
            raise ValueError("Amount must be provided")
        try:
            amount = float(amount)
        except (TypeError,ValueError):
            raise ValueError("Amount must be numeric")
        if amount < 0:
            raise ValueError("Amount must be positive")
        
        perc = max(0.0,min(float(self.__discount_percentage),100.0))
        return amount * (perc/100) 
    
    def discounted_price(self,amount):
        """Return final price after applying discount (never negative)."""

        discount = self.discount_amount(amount)
        return max(amount-discount,0.0)

    def discount_for_line(self,product,quantity=1):
         """Return discount value for a product line (price * qty) if coupon applies."""

         if not self.applies_to(product.product_id):
             return 0.0
         line_total = product.price * quantity
         return self.discount_amount(line_total)

    def __repr__(self):
        return f"<Coupon {self.__code} - {self.__discount_percentage}%>"
