from src.models.sqlite.interfaces.orders_repository import OrdersRepositoryInterface

class OrderRegistryController:
    def __init__(self, orders_repository: OrdersRepositoryInterface):
        self.__orders_repository = orders_repository

    def registry(self, order_info: dict) -> dict:
        user_id = order_info["user_id"]
        description = order_info["description"]
        date = order_info["date"]

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

