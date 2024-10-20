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

@user_bp.route('/users/<user_id>', methods=["GET"])
def get_user(user_id):
    facade = current_app.config['FACADE']
    try:
        user = facade.user_facade.get_user(user_id)
    except ValueError as e:
        abort(404, "e")
    return user

@user_bp.route('/users/<user_id>', methods=["PUT"])
def update_user(user_id):
    facade = current_app.config['FACADE']
    updated_data = request.get_json()
    try:
        updated_user = facade.user_facade.update_user(user_id, updated_data)
    except ValueError as e:
        abort(400, "e")
    return updated_user

@user_bp.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    facade = current_app.config['FACADE']
    user = facade.user_facade.get_user(user_id)
    try:
        facade.user_facade.delete_user(user_id)
    except ValueError as e:
        abort(400, "e")
    return (f"Deleted user: {user}")
 