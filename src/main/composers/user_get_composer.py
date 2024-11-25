from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.models.sqlite.repositories.user_repository import UserRepository
from src.controllers.user_get_controller import GetUserController
from src.views.user_get_view import GetUserView

def get_user_composer():
    conn = db_connection_handler.get_connection()
    model = UserRepository(conn)
    controller = GetUserController(model)
    view = GetUserView(controller)

    return view