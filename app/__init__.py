import os
from flask import Flask
from flask_restx import Api
from config import config 
from app.api.v1.routes_users import user_bp 
from app.services.facade import HBnBFacade

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app, version="1.0", title="HBnB API", description="HBnB application API")

    app.config['FACADE'] = HBnBFacade(app.config)

    app.register_blueprint(user_bp)

    return app