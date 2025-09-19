class AuthUtils:
    users_db = {}  

    @classmethod
    def register_user(cls, email, password, name, role):
        
        pass

    @classmethod
    def login(cls, email, password):
        
        pass

    @classmethod
    def logout(cls, user):
        
        pass

    @staticmethod
    def hash_password(password):
        pass

    @staticmethod
    def verify_password(hashed_password, plain_password):
        pass
