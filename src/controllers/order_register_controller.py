from src.models.sqlite.interfaces.orders_repository import OrdersRepositoryInterface
from .interfaces.order_register_controller import OrderRegisterControllerInterface

class OrderRegisterController(OrderRegisterControllerInterface):
    def __init__(self, orders_repository: OrdersRepositoryInterface):
        self.__orders_repository = orders_repository

    def registry(self, user_id: int, description: str, date: str) -> dict:

        self.__registry_in_db(user_id, description, date)

        formated_response = self.__format_response(description, date)

        return formated_response

    def __registry_in_db(self, user_id: int, description: str, date: str) -> None:
        self.__orders_repository.registry_order(user_id, description, date)

    def __format_response(self, description: str, date: str) -> None:
        return {
            "data": {
                "type": "order",
                "count": 1,
                "details": {
                    "description": description,
                    "date": date
                }
            }
        }

