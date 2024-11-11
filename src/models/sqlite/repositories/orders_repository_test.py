from .orders_repository import OrdersRepository
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
    user_id = 1
    description = "alguma coisa"
    date = "12/12/06"

    mock_connection = MockConnection()
    repo = OrdersRepository(mock_connection)

    repo.registry_order(user_id, description, date)

    cursor = mock_connection.cursor.return_value
    
    assert "INSERT INTO orders" in cursor.execute.call_args[0][0]
    assert "(user_id, description, date)" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id, description, date)
    mock_connection.commit.assert_called_once()


def test_list_orders():
    user_id = 1

    mock_connection = MockConnection()
    repo = OrdersRepository(mock_connection)

    repo.list_orders(user_id)

    cursor = mock_connection.cursor.return_value

    print(cursor.execute.call_args[0])

    assert "SELECT description, date" in cursor.execute.call_args[0][0]
    assert "FROM orders" in cursor.execute.call_args[0][0]
    assert "WHERE user_id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_id,)
    # cursor.fetchone.assert_called_once()
