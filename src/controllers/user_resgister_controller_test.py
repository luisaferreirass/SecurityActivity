import pytest
from .user_register_controller import UserRegisterController
from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.user_repository import UserRepository

# db_connection_handler.connect()

@pytest.mark.skip(reason= "interação com o banco ")
def test_registry_user():
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    controller = UserRegisterController(repo)

    username = "Luisa"
    password = "Luilove16"
    
    controller.registry(username, password)

class MockRepository:
    def __init__(self):
        self.registry_user_attributes = {}

    def registry_user(self, username: str, password: str) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password


def test_registry():
    repository = MockRepository()
    controller = UserRegisterController(repository)

    username = "Luisa"
    password = "Luisa123"

    response = controller.registry(username, password)

    print(response)

    assert response["data"]["type"] == "User"
    assert response["data"]["username"] == username

    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password

    
