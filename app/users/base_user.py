from abc import ABC , abstractmethod

class User(ABC):
    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.name = name
        self.role = None

    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,new_email):
        self.__email = new_email

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password
    
    @abstractmethod
    def view_menu(self,products, coupons = None):
        pass

    def __repr__(self):
        return f"<User role={self.role}, email={self.__email}>"


    


