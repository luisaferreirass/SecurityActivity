import bycript

class PasswordHandler:

    def encrypt_password(self, password: str) -> str:
        salt = bycript.gentsalt()

        hashed_password = bycript.hashpw(password.encode("utf-8"), salt)
        return hashed_password
    
    def check_password(self, password: str, hashed_password: str) -> bool:
        return bycript.checkpw(password.encode("utf8", hashed_password))