from flask import Flask 
from src.models.sqlite.settings.db_connection_handler import db_connection_handler
from

db_connection_handler.connect()

app = Flask(__name__)