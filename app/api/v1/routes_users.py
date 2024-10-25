# routes_users.py

from flask import Blueprint, current_app, request, abort
from flask_restx import Api, Namespace, Resource, fields

users_bp = Blueprint('users', __name__)
api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'type': fields.String(required=False, description='Type will be given in response', example='user'),
    'id': fields.String(required=False, description='id given in the response', example=''),
    'first_name': fields.String(required=True, description='First name', example='Johnny'),
    'last_name': fields.String(required=True, description='Last name', example='Rocker'),
    'email': fields.String(required=True, description='Email address', example='Johnny.rocker@gmail.com'),
    'password' : fields.String(required=True, description="Password", example='mypassword'),
    'is_admin': fields.Boolean(required=True, description='Admin rights', example='false'),
    'created_at': fields.String(required=False, description='Time of creation, given in response', example=''),
    'updated_at': fields.String(required=False, description='Time of update, given in response', example=''),
})

@api.route('/home')
class Home(Resource):
    def get(self):
        return "Welcome to the homepage"
    
 #   <------------------------------------------------------------------------>


@api.route('/')
class UserList(Resource):
    @api.doc('create_user')
    @api.expect(user_model)
    @api.marshal_with(user_model, code=201) # type: ignore
    def post(self):
        """Create a new user"""
        facade = current_app.extensions['HBNB_FACADE']
        new_user = request.get_json()
        try:
            user = facade.user_facade.create_user(new_user)
        except ValueError as e:
            abort(400, str(e))
        if user is None:
            abort(400, "User already exists")
        return user, 201
    
    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        facade = current_app.extensions['HBNB_FACADE']
        users = facade.user_facade.get_all_users()
        return users
    

@api.route('/<string:user_id>')
@api.param('user_id', 'The User identifier')
class UserResource(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get a user by ID"""
        facade = current_app.extensions['HBNB_FACADE']
        user = facade.user_facade.get_user(user_id)
        if not user:
            abort(404, "User not found")
        return user

    @api.doc('update_user')
    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a user"""
        facade = current_app.extensions['HBNB_FACADE']
        updated_data = request.get_json()
        try:
            updated_user = facade.user_facade.update_user(user_id, updated_data)
        except ValueError as e:
            abort(400, str(e))
        if not updated_user:
            abort(404, "User not found")
        return updated_user

    @api.doc('delete_user')
    @api.response(204, 'User deleted')
    def delete(self, user_id):
        """Delete a user"""
        facade = current_app.extensions['HBNB_FACADE']
        user = facade.user_facade.get_user(user_id)
        if not user:
            abort(404, "User not found")
        facade.user_facade.delete_user(user_id)
        return '', 204

 #   <------------------------------------------------------------------------>
