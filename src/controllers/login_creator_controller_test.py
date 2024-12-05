import pytest
from .login_creator_controller import LoginCreatorController
from src.drivers.password_handler import PasswordHandler


username = "nina"
password = "nina123"
hashed_password = PasswordHandler().encrypt_password(password)

class MockRepository():

    def get_user_by_username(self, username: str) -> tuple[int, str, str]:
        return (10, username, hashed_password)
    
def test_login():
    repository = MockRepository()
    controller = LoginCreatorController(repository)

    response = controller.login(username, password)

    assert response["data"]["access"] is True
    assert response["data"]["username"] == username
    assert response["data"]["token"] is not None

def test_login_with_wrong_password():
    repository = MockRepository()
    controller = LoginCreatorController(repository)

    with pytest.raises(Exception):
        controller.login(username, "outraSenha")
