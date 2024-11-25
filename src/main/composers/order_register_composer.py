from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.orders_repository import OrdersRepository
from src.controllers.order_register_controller import OrderRegisterController
from src.views.order_register_view import OrderRegisterView

def order_register_composer():
    conn = db_connection_handler.get_connection()
    model = OrdersRepository(conn)
    controller = OrderRegisterController(model)
    view = OrderRegisterView(controller)

    return view