from flask import Blueprint, current_app, jsonify, request, abort

users_bp = Blueprint('users', __name__)

@users_bp.route('/home', methods=["GET"])
def home():
    return "Welcome to the homepage"

 #   <------------------------------------------------------------------------>


@users_bp.route('/users', methods=["POST"])
def create_user():
    facade = current_app.extensions['HBNB_FACADE']
    new_user = request.get_json()
    try:
        user = facade.user_facade.create_user(new_user)

    except ValueError as e:
        abort(400, str(e))

    if user is None:
        abort(400, "User already exists")
    
    return jsonify(user), 201

 #   <------------------------------------------------------------------------>

@users_bp.route('/users', methods=["GET"])
def get_all_users():
    facade = current_app.extensions['HBNB_FACADE']
    users = facade.user_facade.get_all_users()
    return users

@users_bp.route('/users/<user_id>', methods=["GET"])
def get_user(user_id):
    facade = current_app.extensions['HBNB_FACADE']
    try:
        user = facade.user_facade.get_user(user_id)
    except ValueError as e:
        abort(404, "e")
    return user

 #   <------------------------------------------------------------------------>

@users_bp.route('/users/<user_id>', methods=["PUT"])
def update_user(user_id):
    facade = current_app.extensions['HBNB_FACADE']
    updated_data = request.get_json()
    try:
        updated_user = facade.user_facade.update_user(user_id, updated_data)
    except ValueError as e:
        abort(400, "e")
    return updated_user

 #   <------------------------------------------------------------------------>

@users_bp.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    facade = current_app.extensions['HBNB_FACADE']
    user = facade.user_facade.get_user(user_id)
    try:
        facade.user_facade.delete_user(user_id)
    except ValueError as e:
        abort(400, "e")
    return (f"Deleted user: {user}")
 