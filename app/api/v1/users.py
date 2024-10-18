from flask import Blueprint, jsonify, request, abort
from app.services.facade import HBnBFacade
from app.models.user import User

# Create a blueprint instance for the home routes
user_bp = Blueprint('users', __name__)

facade = HBnBFacade(repo_type="in_file")

@user_bp.route('/home', methods=["GET"])
def home():
    return "Welcome to the homepage"


@user_bp.route('/users', methods=["POST"])
def create_user():
    new_user = request.get_json()
    try:
        user = facade.user_facade.create_user(new_user)

    except ValueError as e:
        abort(400, str(e))

    if user is None:
        abort(400, "User already exists")
    
    return jsonify(user), 201

@user_bp.route('/users', methods=["GET"])
def get_all_users():
    users = facade.user_facade.get_all_users()
    return users