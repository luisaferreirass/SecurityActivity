from abc import ABC, abstractmethod

class OrderListerControllerInterface(ABC):

    @abstractmethod
    def list(self, user_id: int) -> dict:
        pass
