import pytest
from .user_get_controller import GetUserController
from src.models.sqlite.repositories.user_repository import UserRepository
from src.models.sqlite.settings.db_connection_handler import db_connection_handler

# db_connection_handler.connect()

@pytest.mark.skip(reason= "interação com o banco")
def test_get_user():
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    controller = GetUserController(repo)


    user = controller.get_user("nina")

    assert user["data"]["type"] == "User"
    assert user["data"]["details"]["user_id"] == 2
    assert user["data"]["details"]["username"] == "nina"

class MockRepository():
    def get_user_by_username(self, username: str) -> tuple[int, str, str]:
        return (2, username, "$2b$12$fK0huNl56QW/dso4miRzZuU2Wi6YOSJK9eLjr7bmbkidcmS/VQe/m")
    
def test_get():
    repository = MockRepository()
    controller = GetUserController(repository)

    response = controller.get_user("nina")

    assert response["data"]["type"] == "User"
    assert response["data"]["details"]["user_id"] == 2
    assert response["data"]["details"]["username"] == "nina"
