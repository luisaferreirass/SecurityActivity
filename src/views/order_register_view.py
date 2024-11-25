from src.controllers.interfaces.order_register_controller import OrderRegisterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import  ViewInterface


class OrderRegisterView(ViewInterface):
    def __init__(self, controller: OrderRegisterControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.body.get("user_id")
        description = http_request.body.get("description")
        date = http_request.body.get("date")

        self.__validate_input(user_id, description, date)

        response = self.__controller.registry(user_id, description, date)

        return HttpResponse(body= { "data": response}, status_code=201)


    def __validate_input(self, user_id: any, description: any, date: any) -> None:
        if (
            not user_id
            or not description
            or not date
            or not isinstance(user_id, int)
            or not isinstance(description, str)
            or not isinstance(date, str)
        ): raise Exception("Invalid input")