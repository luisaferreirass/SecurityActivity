from flask import Blueprint, jsonify, request
from src.main.composers.order_lister_composer import order_lister_composer
from src.main.composers.order_register_composer import order_register_composer
from src.views.http_types.http_request import HttpRequest
from src.errors.error_handler import handle_errors

order_routes_bp = Blueprint("order_routes", __name__)

@order_routes_bp.route("/order/registry", methods=["POST"])
def order_registry():
    try:
        http_request = HttpRequest(body=request.json)
        view = order_register_composer()

        response = view.handle(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

        return jsonify(http_response.body), http_response.status_code

@order_routes_bp.route("/order/list", methods=["GET"])
def list_orders():
    try:
        http_request = HttpRequest(body=request.json)
        view = order_lister_composer()

        response = view.handle(http_request)

        return jsonify(response.body), response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

        return jsonify(http_response.body), http_response.status_code
