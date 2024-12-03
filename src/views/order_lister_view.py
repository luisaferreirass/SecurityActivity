from src.controllers.interfaces.order_lister_controller import OrderListerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import  ViewInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError


class OrderListerView(ViewInterface):
    def __init__(self, controller: OrderListerControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.body.get("user_id")

        self.__validate_input(user_id)

        response = self.__controller.list(user_id)

        return HttpResponse(body= { "data": response}, status_code=200)


    def __validate_input(self, user_id: any) -> None:

        if not user_id or not isinstance(user_id, int):
            raise HttpBadRequestError("Invalid input")