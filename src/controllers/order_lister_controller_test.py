import pytest
from .order_lister_controller import OrderListerController
from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.orders_repository import OrdersRepository

# db_connection_handler.connect()

@pytest.mark.skip(reason= "interação com o banco")
def test_list_orders():
    conn = db_connection_handler.get_connection()
    repo = OrdersRepository(conn)
    controller = OrderListerController(repo)

    user_id = 1

    response = controller.list(user_id)

    assert response["data"]["type"] == "orders"
    assert response["data"]["count"] is not None
    assert isinstance(response["data"]["details"], list)

class MockRepository():
    def list_orders(self, user_id: int) -> list:
        return [{
            "user_id": user_id,
            "description": "alguma coisa",
            "date": "13/06/2022"
        },
        {
            "user_id": user_id,
            "description": "outra coisa",
            "date": "14/11/2020"
        }]
    
def test_list():
    repository = MockRepository()
    controller = OrderListerController(repository)

    user_id = 2

    response = controller.list(user_id)

    expected_response = {"data": {
        "type": "orders",
        "count": 2,
        "details": [{
            "user_id": 2,
            "description": "alguma coisa",
            "date": "13/06/2022"
        },
        {
            "user_id": 2,
            "description": "outra coisa",
            "date": "14/11/2020"
        }]
    }}


    assert response == expected_response
