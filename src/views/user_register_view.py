from src.controllers.interfaces.user_register_controller import UserRegisterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interface.view_interface import  ViewInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError


class UserRegisterView(ViewInterface):
    def __init__(self, controller: UserRegisterControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")

        self.__validate_input(username, password)

        response = self.__controller.registry(username, password)

        return HttpResponse(body= {"data": response}, status_code=201)

    def __validate_input(self, username: any, password: any) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str)
            or not isinstance(password, str)
        ): raise HttpBadRequestError("Invalid input")
        