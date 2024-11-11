from src.models.sqlite.interfaces.user_repository import UserRepositoryInterface
from .interfaces.user_get_controller import GetUserControllerInterface

class GetUserController(GetUserControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository

    def get_user(self, user_info: dict) -> dict:
        user_id = user_info["user_id"]

        user = self.__get_user_in_db(user_id)

        formated_response = self.__format_response(user)

        return formated_response

    def __get_user_in_db(self, user_id: int) -> tuple[int, str, str]:
        user = self.__user_repository.get_user_by_id(user_id)

        return user
    
    def __format_response(self, user: tuple[int, str, str]) -> dict:
        return {
            "data": {
                "type": "orders", 
                "count": 1, 
                "details": user
            }
        }
