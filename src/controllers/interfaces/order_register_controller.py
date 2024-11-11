from abc import ABC, abstractmethod

class OrderRegisterControllerInterface(ABC):

    @abstractmethod
    def registry(self, order_info: dict) -> dict:
        pass