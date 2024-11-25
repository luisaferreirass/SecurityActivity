from src.drivers.jwt_handler import JWTHandler
from src.drivers.password_handler import PasswordHandler
from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface
from .interfaces.login_creator_controller import LoginCreatorControllerInterface

class LoginCreatorController(LoginCreatorControllerInterface):
    def __init__(self, user_respository: UserRepositoryInterface):
        self.__user_repository = user_respository
        self.__jwt_handler = JWTHandler()
        self.__password_handler = PasswordHandler()

    def login(self, username: str, password: str) -> dict:
        user = self.__find_user_in_db(username)
        user_id = user[0]
        hashed_password = user[2]

        self.__verify_password(password, hashed_password)
        token = self.__create_token(user_id)
        formated_response = self.__format_response(username, token)

        return formated_response

    def __find_user_in_db(self, user_id: int) -> tuple[int, str, str]:
        user = self.__user_repository.get_user_by_id(user_id)

        if not user:
            raise Exception("User not found")
        
        return user
    
    def __verify_password(self, password: str, hashed_password: str) -> None:
        is_password_correct = self.__password_handler.check_password(password, hashed_password)

        if not is_password_correct:
            raise Exception("Wrong password")
        
    def __create_token(self, user_id: int) -> str:
        payload = {"user_id": user_id}

        token = self.__jwt_handler.create_jwt_token(payload)

        return token
    
    def __format_response(self, username: str, token: str) -> dict:
        return {
            "data": {
                "access": True,
                "username": username,
                "token": token
            }
        }