from flask import Flask 
from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from src.main.routes.order_routes import order_routes_bp
from src.main.routes.user_routes import user_route_bp

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(order_routes_bp)
app.register_blueprint(user_route_bp)
