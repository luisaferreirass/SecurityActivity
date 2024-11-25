from abc import ABC, abstractmethod

class OrderRegisterControllerInterface(ABC):

    @abstractmethod
    def registry(self, user_id: int, description: str, date: str) -> dict:
        pass