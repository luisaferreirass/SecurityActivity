from abc import ABC, abstractmethod

class LoginCreatorControllerInterface(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> dict:
       pass
