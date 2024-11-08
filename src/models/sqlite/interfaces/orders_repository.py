from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def registry_order(self, user_id: int, description: str, date: str) -> None:
        pass

    @abstractmethod
    def list_orders(self, user_id: int) -> list:
        pass
