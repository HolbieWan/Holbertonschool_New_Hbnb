import os
from flask import Flask
from flask_restx import Api
from config import config

from app.api.v1.routes_users import users_bp
from app.api.v1.routes_places import places_bp
from app.api.v1.routes_amenities import amenities_bp
from app.api.v1.routes_reviews import reviews_bp

from app.services.facade import HBnBFacade
from app.services.facade_user import UserFacade
from app.services.facade_place import PlaceFacade
from app.services.facade_amenity import AmenityFacade
from app.services.facade_review import ReviewFacade

from app.services.facade_relations_manager import FacadeRelationManager
from app.persistence.repo_selector import RepoSelector

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app, version="1.0", title="HBnB API", description="HBnB application API")

    # Initialize repositories
    repo_type = app.config.get('REPO_TYPE', 'in_memory')
    user_repo_selector = RepoSelector(repo_type, "user_data.json")
    place_repo_selector = RepoSelector(repo_type, "place_data.json")
    amenity_repo_selector = RepoSelector(repo_type, "amenity_data.json")
    review_repo_selector = RepoSelector(repo_type, "review_data.json")

    user_repo = user_repo_selector.select_repo()
    place_repo = place_repo_selector.select_repo()
    amenity_repo = amenity_repo_selector.select_repo()
    review_repo = review_repo_selector.select_repo()

    # Initialize facades
    user_facade = UserFacade(user_repo)
    place_facade = PlaceFacade(place_repo)
    review_facade = ReviewFacade(review_repo)
    amenity_facade = AmenityFacade(amenity_repo)

    # Initialize HBnBFacade with existing facades
    hbnb_facade = HBnBFacade(user_facade, place_facade, amenity_facade, review_facade)

    # Store hbnb_facade and other facades in app.extensions
    app.extensions['HBNB_FACADE'] = hbnb_facade
    app.extensions['FACADE_RELATION_MANAGER'] = FacadeRelationManager(user_facade, place_facade, amenity_facade, review_facade)

    # Register blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(amenities_bp)
    app.register_blueprint(reviews_bp)

    return app