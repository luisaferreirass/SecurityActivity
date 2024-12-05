from .jwt_handler import JWTHandler

def test_jwt_handle():
    jwt_handler = JWTHandler()
    body = {
        "username": "Luisa",
        "aqui": "estou aqui",
        "lalala": ""
    }

    token = jwt_handler.create_jwt_token(body)
    token_information = jwt_handler.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_information["username"] == body["username"]
    assert token_information["lalala"] == body["lalala"]

    print()
    print(token)
    print()
    print(token_information)
