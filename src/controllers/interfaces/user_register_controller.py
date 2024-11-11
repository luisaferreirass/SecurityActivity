from abc import ABC, abstractmethod

class UserRegisterControllerInterface(ABC):

    @abstractmethod
    def registry(self, user_info: dict) -> dict:
        pass