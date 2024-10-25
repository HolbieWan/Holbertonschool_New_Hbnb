from flask import Blueprint, current_app, jsonify, request, abort
from flask_restx import api, Namespace, Resource, fields

amenities_bp = Blueprint('amenities', __name__)
api = Namespace('amenities', description='Amenity operations')

amenity_model = api.model('Amenity', {
    'type': fields.String(required=False, description='Type will be given in response', example='amenity'),
    'id': fields.String(required=False, description='Id will be given in response', example=''),
    'name': fields.String(required=True, description='Name of the amenity', example='Sauna'),
    'created_at': fields.String(required=False, description='Time of creation, given in response', example=''),
    'updated_at': fields.String(required=False, description='Time of update, given in response', example=''),
})

#   <------------------------------------------------------------------------>

@api.route('/')
class AmenityList(Resource):
    @api.doc('create_amenity')
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201) #type: ignore
    def post(self):
        """Create a new amenity"""
        facade = current_app.extensions['HBNB_FACADE']
        new_amenity = request.get_json()
        
        try:
            amenity = facade.amenity_facade.create_amenity(new_amenity)
        except ValueError as e:
            abort(400, "Amenity already exists")
        if amenity is None:
            abort(400, "Amenity already exist")

        return amenity, 201
    
    @api.doc('get_all_amenities')
    @api.marshal_with(amenity_model, code=201) #type: ignore
    def get(self):
        """Get a list of all amenities"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            amenities = facade.amenity_facade.get_all_amenities()
        except ValueError as e:
            abort(400, "e")
        return amenities

#   <------------------------------------------------------------------------>

@api.route('/<string:amenity_id>')
@api.param('amenity_id', 'The amenity identifier')
class Amenity(Resource):
    @api.doc('get_amenity')
    @api.marshal_with(amenity_model) # type: ignore
    def get(self, amenity_id):
        """Get an amenity by id"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            amenity = facade.amenity_facade.get_amenity(amenity_id)
        except ValueError as e:
            abort(404, "e")
        return amenity, 200

    @api.doc('update_amenity')
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model) # type: ignore
    def put(self, amenity_id):
        """Update an amenity"""
        facade = current_app.extensions['HBNB_FACADE']
        updated_data = request.get_json()
        try:
            updated_amenity = facade.amenity_facade.update_amenity(amenity_id, updated_data)
        except ValueError as e:
            abort(404, "e")
        return updated_amenity, 200
    
    @api.doc('delete_amenity')
    @api.marshal_with(amenity_model) # type: ignore
    def delete(self, amenity_id):
        """Delete an amenity"""
        facade = current_app.extensions['HBNB_FACADE']
        amenity_to_delete = facade.amenity_facade.get_amenity(amenity_id)
        try:
            facade.amenity_facade.delete_amenity(amenity_id)
        except ValueError as e:
            abort(400, "e")
        return (f"Amenity: {amenity_to_delete} has been deleted."), 200

#   <------------------------------------------------------------------------>

# @amenities_bp.route('/<place_id>/amenities', methods=["POST"])
# def create_amenity_for_place(place_id):
#     facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
#     new_amenity = request.get_json()
    
#     try:
#         amenity = facade_relation_manager.create_amenity_for_place(place_id, new_amenity)

#     except ValueError as e:
#         abort(400, "e")

#     return amenity, 201

# #   <------------------------------------------------------------------------>

# @amenities_bp.route('/places/<place_id>/amenities', methods=["GET"])
# def get_all_amenities_id_from_place(place_id):
#     facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
#     try:
#         amenities = facade_relation_manager.get_all_amenities_names_from_place(place_id)
#     except ValueError as e:
#         abort(400, "e")
#     return jsonify(amenities), 200

# #   <------------------------------------------------------------------------>

# @amenities_bp.route('/place/<place_id>/amenity/<amenity_id>', methods=["DELETE"])
# def delete_amenity_from_place_list(place_id, amenity_id):
#     facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']

#     try:
#         facade_relation_manager.delete_amenity_from_place_list(amenity_id, place_id)
#     except ValueError as e:
#         abort(400, str(e))

#     return jsonify({"message": f"Amenity: {amenity_id} has been deleted from amenities list"}), 200

#  #   <------------------------------------------------------------------------>