import hashlib

class AuthUtils:
    users_db = {}  

    @classmethod
    def register_user(cls, email, password, name, role):
        cls.users_db[email] = {
                "name": name,
                "role": role,
                "password": cls.hash_password(password),
            }
        return cls.users_db

    @classmethod
    def login(cls, email, password):
        if email in cls.users_db:
            stored_hash = cls.users_db[email]["password"]
            if cls.verify_password(stored_hash,password):
                return f"Login successful"
        return "Login failed"

    @classmethod
    def logout(cls, email):
        if email in cls.users_db:
            return f"{email} logged out"
        return "User not found"

    @staticmethod
    def hash_password(password):
        hashing_alg = hashlib.sha512()
        hashing_alg.update(password.encode())
        return hashing_alg.hexdigest()


    @staticmethod
    def verify_password(hashed_password, plain_password):
        hashing_alg = hashlib.sha512()
        hashing_alg.update(plain_password.encode())
        return hashed_password == hashing_alg.hexdigest()
