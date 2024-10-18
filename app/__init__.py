from flask import Flask
from flask_restx import Api
from app.api.v1.users import user_bp 

def create_app():
    app = Flask(__name__)
    api = Api(app, version="1.0", title="HBnB API", description="HBnB application API")

    # Placeholder for API namespaces (endpoints will be added later)
    # Additional namespaces for places, reviews, and amenities will be added later
    app.register_blueprint(user_bp)

    return app