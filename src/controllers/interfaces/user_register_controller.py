from abc import ABC, abstractmethod

class UserRegisterControllerInterface(ABC):

    @abstractmethod
    def registry(self, username: str, password: str) -> dict:
        pass