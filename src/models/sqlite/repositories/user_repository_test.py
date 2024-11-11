from .user_repository import UserRepository
from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from unittest.mock import Mock

class MockCursor:
    def __init__(self):
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self):
        
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_registry():
    username = "Luisa"
    password = "Luilove16"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username, password)

    cursor = mock_connection.cursor.return_value

    
    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password)" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password)
    mock_connection.commit.assert_called_once()


def test_get_user_by_id():
    
    user_id = 1

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_id(user_id)

    cursor = mock_connection.cursor.return_value

    print(cursor.execute.call_args[0])

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id,)
    cursor.fetchone.assert_called_once()
