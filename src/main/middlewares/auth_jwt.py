from flask import request
from src.drivers.jwt_handler import JWTHandler
from src.errors.error_types.http_unathorized import HttpUnauthorizedError

def auth_jwt_verify():
    jwt_handler = JWTHandler()
    raw_token = request.headers.get("Authorization")
    username = request.headers.get("username")

    if not raw_token or not username:
        raise HttpUnauthorizedError("Invalid auth informations")
    
    token = raw_token.split()[1]

    token_information = jwt_handler.decode_jwt_token(token)
    token_uname = token_information.get("username")
    
    if username and token_uname and (username == token_uname):
        return token_information
    
    raise HttpUnauthorizedError("User unauthorized")