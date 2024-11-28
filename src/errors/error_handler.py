from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_unathorized import HttpUnauthorizedError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnauthorizedError)):
        return  HttpResponse(
            body= {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }, status_code=error.status_code
        )
    
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server error",
                "detail": str(error)
            }]
        }
    )
