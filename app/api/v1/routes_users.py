from flask import Blueprint, current_app, jsonify, request, abort
from app.services.facade import HBnBFacade

user_bp = Blueprint('users', __name__)

@user_bp.route('/home', methods=["GET"])
def home():
    return "Welcome to the homepage"


@user_bp.route('/users', methods=["POST"])
def create_user():
    facade = current_app.config['FACADE']
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
    facade = current_app.config['FACADE']
    users = facade.user_facade.get_all_users()
    return users