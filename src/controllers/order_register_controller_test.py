import pytest
from .order_register_controller import OrderRegisterController
from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.orders_repository import OrdersRepository

# db_connection_handler.connect()

@pytest.mark.skip(reason=" interação com o banco ")
def test_registry_orders():
    conn = db_connection_handler.get_connection()
    repo = OrdersRepository(conn)
    controller = OrderRegisterController(repo)

    user_id = 1
    description = "outro pedido"
    date = "11/03/2022"


    controller.registry(user_id, description, date)

class MockRepository():
    def __init__(self):
        self.registry_order_attributes = {}

    def registry_order(self, user_id: int, description: str, date: str) -> None:
        self.registry_order_attributes["user_id"] = user_id
        self.registry_order_attributes["description"] = description
        self.registry_order_attributes["date"] = date

def test_registry():
    repository = MockRepository()
    controller = OrderRegisterController(repository)


    user_id = 2
    description = "alguma coisa"
    date = "12/08/2023"

    response = controller.registry(user_id, description, date)

    assert response["data"]["type"] == "order"
    assert response["data"]["details"]["description"] == description
    assert response["data"]["details"]["date"] == date

    assert repository.registry_order_attributes["user_id"] == user_id
    assert repository.registry_order_attributes["description"] == description
    assert repository.registry_order_attributes["date"] == date