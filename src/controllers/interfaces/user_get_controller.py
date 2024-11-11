from abc import ABC, abstractmethod

class GetUserControllerInterface(ABC):
    
    @abstractmethod
    def get_user(self, user_info: dict) -> dict:
        pass