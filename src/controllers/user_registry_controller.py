from src.drivers.password_handler import PasswordHandler
from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface

class UserRegistryController:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry(self, user_info: dict) -> dict:
        username = user_info["username"]
        password = user_info["password"]
        hashed_password = self.__encrypt_password(password)

        self.__registry_in_db(username, hashed_password)

        formated_response = self.__format_response(username)

        return formated_response

    def __encrypt_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password)

        return hashed_password
    
    def __registry_in_db(self, username: str, hashed_password: str) -> None:
        self.__user_repository.registry_user(username, hashed_password)

    def __format_response(self, username: str) -> dict:
        return {
            "data": {
                "type": "User",
                "count": 1,
                "username": username
            }
        }
