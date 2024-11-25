from abc import ABC, abstractmethod

class GetUserControllerInterface(ABC):
    
    @abstractmethod
    def get_user(self, username: str) -> dict:
        pass