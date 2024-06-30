from flask import Flask
from app.views import *
from app.database import init_app
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    init_app(app)
    CORS(app)

    app.route('/api/countries/', methods=['GET'])(get_all_countries)
    app.route('/api/users/', methods=['POST'])(create_user)
    app.route('/api/users/login', methods=['POST'])(login_user)
    app.route('/api/users/<int:id>', methods=['PUT'])(update_lastlogin)
    app.route('/api/users/<int:id>', methods=['DELETE'])(delete_user)
    
    return app
