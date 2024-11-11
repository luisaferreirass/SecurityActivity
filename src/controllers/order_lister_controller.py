from src.models.sqlite.interfaces.orders_repository import OrdersRepositoryInterface

class OrderListerController:
    def __init__(self, orders_repository : OrdersRepositoryInterface):
        self.__orders_repository = orders_repository

    def list(self, user_info: dict) -> dict:
        user_id = user_info["user_id"]

        list_orders = self.__list_in_db(user_id)

        formated_response = self.__format_response(list_orders)

        return formated_response

    def __list_in_db(self, user_id: int) -> list:
        list_orders = self.__orders_repository.list_orders(user_id)

        return list_orders
    
    def __format_response(self, list_orders: list):
        return {
            "data": {
                "type": "orders",
                "count": len(list_orders),
                "detaisl": list_orders
            }
        }