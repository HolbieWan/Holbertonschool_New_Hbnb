# routes_users.py

from flask import Blueprint, current_app, request, abort
from flask_restx import Api, Namespace, Resource, fields
from email_validator import EmailNotValidError

users_bp = Blueprint('users', __name__)
api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'type': fields.String(required=False, description='Type will be given in response', example='user'),
    'id': fields.String(required=False, description='id given in the response', example=''),
    'first_name': fields.String(required=True, description='First name', example='Johnny'),
    'last_name': fields.String(required=True, description='Last name', example='Rocker'),
    'email': fields.String(required=True, description='Email address', example='johnny.rocker@gmail.com'),
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
        user_data = request.get_json()
        try:
            new_user = facade.user_facade.create_user(user_data)

            user_response = {
            "type": new_user["type"],
            "id": new_user["id"],
            "first_name": new_user["first_name"],
            "last_name": new_user["last_name"],
            "email": new_user["email"],
            "password": "****",
            "is_admin": new_user["is_admin"],
            "created_at": "",
            "updated_at": ""
            }
            return user_response, 201

        except ValueError as e:
            abort(400, str(e))
    
    @api.doc('list_users')
    @api.marshal_list_with(user_model)
    def get(self):
        """Get all users"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            users = facade.user_facade.get_all_users()
            if not users:
                raise ValueError("No user found")
            return users, 200

        except ValueError as e:
            abort(400, str(e))
    
@api.route('/<string:user_id>')
@api.param('user_id', 'The User identifier')
class UserResource(Resource):
    @api.doc('get_user')
    @api.marshal_with(user_model)
    def get(self, user_id):
        """Get a user by ID"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            user = facade.user_facade.get_user(user_id)
            return user, 200
        
        except ValueError as e:
            abort(400, str(e))

    @api.doc('update_user')
    @api.expect(user_model)
    @api.marshal_with(user_model)
    def put(self, user_id):
        """Update a user"""
        facade = current_app.extensions['HBNB_FACADE']
        updated_data = request.get_json()
        try:
            updated_user = facade.user_facade.update_user(user_id, updated_data)
            return updated_user, 200
        
        except ValueError as e:
            abort(400, str(e))

    @api.doc('delete_user')
    @api.response(204, 'User deleted')
    def delete(self, user_id):
        """Delete a user"""
        facade = current_app.extensions['HBNB_FACADE']

        try:
            facade.user_facade.delete_user(user_id)
            return {"message": f"User: {user_id} has been deleted"}, 200
        
        except ValueError as e:
            abort(400, str(e))

 #   <------------------------------------------------------------------------>
