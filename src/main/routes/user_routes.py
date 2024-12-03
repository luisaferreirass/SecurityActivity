from flask import Blueprint, jsonify, request
from src.main.composers.user_get_composer import get_user_composer
from src.main.composers.user_register_composer import user_register_composer
from src.main.composers.login_creator_composer import login_creator_composer
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors
from src.main.middlewares.auth_jwt import auth_jwt_verify

user_route_bp = Blueprint("user_routes", __name__)

@user_route_bp.route("/user/registry", methods=["POST"])
def registry_user():
    try:
        http_request = HttpRequest(body=request.json)
        view = user_register_composer()
        response = view.handle(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

        return jsonify(http_response.body), http_response.status_code

@user_route_bp.route("/user/get/<username>", methods=["GET"])
def get_user(username):
    try:
        token_information = auth_jwt_verify()
        http_request = HttpRequest(body=request.json,
        token_infos= token_information,
        headers=request.headers,
        params= {"username": username})
        view = get_user_composer()
        response = view.handle(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

        return jsonify(http_response.body), http_response.status_code

@user_route_bp.route("/user/login", methods=["POST"])
def login_user():
    try:
        http_request = HttpRequest(body=request.json)
        
        view = login_creator_composer()
        
        response = view.handle(http_request)
    

        return jsonify(response.body), response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

        return jsonify(http_response.body), http_response.status_code
