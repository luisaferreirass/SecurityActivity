from abc import ABC, abstractmethod

class OrderListerControllerInterface(ABC):

    @abstractmethod
    def list(self, user_info: dict) -> dict:
        pass
