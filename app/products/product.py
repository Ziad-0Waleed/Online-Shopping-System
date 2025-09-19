from datetime import datetime

class Product:
    def __init__(self, product_id, name, price, stock, expiry_date=None):

        self.product_id = product_id
        self.name = name
        self.__price = price
        self.__stock = stock
        self.__expiry_date = (
            datetime.strptime(expiry_date , '%Y-%m-%d').date()
            if expiry_date else None
        )

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            raise ValueError("Price must be positive")
        
    @property    
    def stock(self):
        return self.__stock
    
    @property
    def expiry_date(self):
        return self.__expiry_date
    
    def add_stock(self, quantity):
        if quantity > 0:
            self.__stock += quantity
        else:
            raise ValueError("Quantity must be positive")
        
    def reduce_stock(self, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        else:
            if self.__stock >= quantity :
                self.__stock -= quantity
            else:
                raise ValueError("Not enough stock available")
                

    def is_available(self):
        return self.__stock > 0

    def is_expired(self):
        if self.expiry_date is None:
            return False
        else:
            return self.expiry_date < datetime.today().date()

    def __repr__(self):
        
        return f"Product name → '{self.name}', Product ID : '{self.product_id}', Product price → ${self.__price}, Available stock → {self.__stock}, Expiry date → {self.expiry_date}"
    


