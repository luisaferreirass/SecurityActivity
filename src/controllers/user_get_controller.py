from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface
from .interfaces.user_get_controller import GetUserControllerInterface

class GetUserController(GetUserControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository

    def get_user(self, username: str) -> dict:
        
        user = self.__get_user_in_db(username)

        formated_response = self.__format_response(user)

        return formated_response

    def __get_user_in_db(self, username: str) -> tuple[int, str, str]:
        user = self.__user_repository.get_user_by_id(username)

        return user
    
    def __format_response(self, user: tuple[int, str, str]) -> dict:
        return {
            "data": {
                "type": "orders", 
                "count": 1, 
                "details": user
            }
        }
