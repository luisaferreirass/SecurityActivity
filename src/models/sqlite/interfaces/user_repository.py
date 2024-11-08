from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def registry_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> tuple[int, str, str]:
        pass
