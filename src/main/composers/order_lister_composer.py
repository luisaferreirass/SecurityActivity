from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.orders_repository import OrdersRepository
from src.controllers.order_lister_controller import OrderListerController
from src.views.order_lister_view import OrderListerView

def order_lister_composer():
    conn = db_connection_handler.get_connection()
    model = OrdersRepository(conn)
    controller = OrderListerController(model)
    view = OrderListerView(controller)

    return view