from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.controllers.interfaces.user_get_controller import GetUserControllerInterface
from .interface.view_interface import  ViewInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError



class GetUserView(ViewInterface):
    def __init__(self, controller: GetUserControllerInterface):
        self.__controller = controller


    def handle(self, http_request: HttpRequest) -> HttpResponse:
        username = http_request.params.get("username") 

        self.__validate_input(username)

        response = self.__controller.get_user(username)

        return HttpResponse(body= {"data": response}, status_code=200)


    def __validate_input(self, username: any) -> None:
        if not username or not isinstance(username, str):
            raise HttpBadRequestError("Invalid input")

