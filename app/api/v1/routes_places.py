from flask import Blueprint, current_app, jsonify, request, abort
from flask_restx import api, Namespace, Resource, fields

places_bp = Blueprint('places', __name__)
api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'type': fields.String(required=False, description='Type will be given in response', example='place'),
    'id': fields.String(required=False, description='Id will be given in response', example=''),
    'title': fields.String(required=True, description='Name of the place', example='Chez Johnny'),
    'amenities': fields.List(fields.String, required=False, description='List of amenities', example=["BBQ", "Jacuzzi"]),
    'reviews': fields.List(fields.String, required=False, description='List of reviews', example=[""]),
    'price': fields.Float(required=True, description='Price per night', example='150.50'),
    'description': fields.String(required=True, description='Description of the place', example='The rocker place'),
    'latitude': fields.Float(required=True, description='Latitude coordonates of the place', example='23.2356'),
    'longitude': fields.Float(required=True, description='Longitude coordinates of the place', example='54.4577'),
    'owner_first_name': fields.String(required=False, description='First_name of the owner of those places', example="Johnny"),
    'owner_id': fields.String(required=True, description='Id of the owner of the place', example='0defc403-97f3-4784-83c2-363dd7982c61'),
    'created_at': fields.String(required=False, description='Time of creation, given in response', example=''),
    'updated_at': fields.String(required=False, description='Time of update, given in response', example=''),
})

# extended_place_model = api.inherit('ExtendedPlace', place_model, {
#     'owner_name': fields.String(required=False, description='Name of the owner of those places')
# })

place_creation_model = api.model('Place_creation', {
    'title': fields.String(required=True, description='Name of the place', example='Chez Johnny'),
    'price': fields.Float(required=True, description='Price per night', example='150.50'),
    'description': fields.String(required=True, description='Description of the place', example='The rocker place'),
    'latitude': fields.Float(required=True, description='Latitude coordonates of the place', example='23.2356'),
    'longitude': fields.Float(required=True, description='Longitude coordinates of the place', example='54.4577'),
    'amenities': fields.List(fields.String, required=False, description='List of amenities', example=["BBQ", "Jacuzzi"]),
    'reviews': fields.List(fields.String, required=False, description='List of reviews', example=[""]),
    'owner_first_name': fields.String(required=False, description='First_name of the owner of those places', example="Johnny"),
    'owner_id': fields.String(required=True, description='Id of the owner of the place', example='0defc403-97f3-4784-83c2-363dd7982c61'),
})

add_amenity_model = api.model('Add_amenity_model', {
    'name': fields.String(required=True, description='Name of the amenity', example='Sauna'),
    'place_id': fields.String(required=True, description='Id of the place to append', example='')
})

get_amenities_model = api.model('Get_amenities_model', {
    'place_id': fields.String(required=False, description='Id of the place to retrieve from', example=''),
    'place_amenities': fields.List(fields.String, required=False, description='List of amenities for a place', example=['Sauna'])
})

add_review_model = api.model('Add_review_model', {
    'user_id': fields.String(required=True, description='User_id of the poster', example='007c0cdd-c2d1-4232-b262-6314522aca45'),
    'user_first_name': fields.String(required=True, description='First_name of the poster', example='Johnny'),
    'text': fields.String(required=True, description='Text content for the new review', example='Great place for a relaxing time'),
    'rating': fields.Integer(required=True, description='Rating of the place, from 1 to 5', example='4'),
    'place_id': fields.String(required=True, description='Id of the place to append', example='87991657-0570-4f97-9641-2052812d924b'),
    'place_name': fields.String(required=True, description='Name of the reviewed place', example='Chez Johnny 3'),
})

get_all_reviews_success_model = api.model('GetAllReviews', {
    # 'place_id': fields.String(required=False, description='Id of the place to retrieve from', example=''),
    # 'place_name': fields.String(required=False, description='Name of the place', example='Chez Johnny'),
    'reviews': fields.List(fields.Nested(api.model('Review', {
        # 'place_name': fields.String,
        'user_id': fields.String(required=False, description='User_id of the reviewer', example='007c0cdd-c2d1-4232-b262-6314522aca45'),
        'user_first_name': fields.String(required=False, description='First_name of the reviewer', example='Johnny'),
        'text': fields.String(required=False, description='Content of the review', example='Very nice'),
        'rating': fields.Integer(required=False, description='Rating of the place from 1 to 5', example='4'),
    })), required=False, description='List of reviews for the place', example=[{}]),
})


@api.route('/')
class PlaceList(Resource):
    # @api.doc('create_place')
    # @api.expect(place_model)
    # @api.marshal_with(place_model, code=201) # type: ignore
    # def post(self):
    #     """Create a new place for a user"""
    #     facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
    #     new_place_data = request.get_json()
    #     user_id = new_place_data["owner_id"]
    #     try:
    #         place = facade_relation_manager.create_place_for_user(user_id, new_place_data)
    #         return place, 201

    #     except ValueError as e:
    #         abort(400, str(e))
    
    @api.doc('get_all_places')
    @api.marshal_list_with(place_model)
    def get(self):
        """Get all places"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            places = facade.place_facade.get_all_places()
            if not places:
                raise ValueError(f"No place found")
            return places, 200

        except ValueError as e:
            abort(400, str(e))

 #   <------------------------------------------------------------------------>

@api.route('/<string:place_id>')
@api.param('place_id', 'The place identifier')
class PlaceResource(Resource):
    @api.doc('get_place')
    @api.marshal_with(place_model)
    def get(self, place_id):
        """Get a place by id"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            place = facade.place_facade.get_place(place_id)
            return place, 200
        
        except ValueError as e:
            abort(404, str(e))
    
    @api.doc('update_place')
    @api.expect(place_model)
    @api.marshal_with(place_model)
    def put(self, place_id):
        """Update a place by id"""
        facade = current_app.extensions['HBNB_FACADE']
        updated_data = request.get_json()
        try:
            updated_place = facade.place_facade.update_place(place_id, updated_data)
            return updated_place, 200
        
        except ValueError as e:
            abort(400, str(e))
    
    @api.doc('delete_place')
    @api.marshal_with(place_model)
    def delete(self, place_id):
        """Delete a place"""
        facade = current_app.extensions['HBNB_FACADE']
        
        try:
            facade.place_facade.delete_place(place_id)
            return {"message": f"Place: {place_id} has been deleted"}, 200
        
        except ValueError as e:
            abort(400, str(e))

 #   <------------------------------------------------------------------------>

# @api.route('/<string:owner_id>/places')
# @api.param('owner_id')
# class PlaceOwnerDetails(Resource):
#     @api.doc('get_places_by_owner')
#     @api.marshal_with(place_model)
#     def get(self, owner_id):
#         """Get all places from the owner_id"""
#         facade = current_app.extensions['HBNB_FACADE']
#         try:
#             places = facade.place_facade.get_all_places_from_owner_id(owner_id)
#         except ValueError as e:
#             abort(400, str(e))
#         return places, 200

# #   <------------------------------------------------------------------------>

# @api.route('/<string:user_id>/places')
# @api.param('user_id')
# class PlaceOwnerAndUserDetails(Resource):
#     @api.doc('get_places_by_user_id')
#     @api.marshal_with(place_model)
#     def get(self, user_id):
#         """Get all places from the user_id"""
#         facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
#         try:
#             places = facade_relation_manager.get_all_places_from_user_id(user_id)
#         except ValueError as e:
#             abort(400, str(e))
#         return places, 200

# #   <------------------------------------------------------------------------>

@api.route('/<string:place_id>/user')
@api.param('place_id')
class PlaceUserOwnerDetails(Resource):
    @api.doc('delete_place_in_place_repo_and_user_repo')
    def delete(self, place_id):
        """Delete a place in place repo and user repo"""
        facade = current_app.extensions['HBNB_FACADE']
        facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']

        try:
            place = facade.place_facade.get_place(place_id)
            user_id = place.get("owner_id")
            facade_relation_manager.delete_place_from_owner_place_list(place_id, user_id)
            return (f"Place: {place_id} has been deleted")

        except ValueError as e:
            abort(400, str(e))


 #   <------------------------------------------------------------------------>


@api.route('/<string:place_id>/amenities')
@api.param('place_id', 'The place identifier')
class AmenityPlaceList(Resource):
    @api.doc('add_amenity_to_a_place')
    @api.expect(add_amenity_model)
    @api.marshal_with(add_amenity_model) # type: ignore
    def post(self, place_id):
        """Add an amenity to a place"""
        facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']

        try:
            amenity_data = request.get_json()
            amenities = facade_relation_manager.add_amenity_to_a_place(place_id, amenity_data)
            amenities["place_id"] = place_id
            print(amenities)

        except ValueError as e:
            abort(400, str(e))
        
        return amenities, 201


    @api.doc('get_all_amenity_names_for_a_place')
    @api.marshal_with(get_amenities_model) # type: ignore
    def get(self, place_id):
        """Get all amenity names for a place"""
        facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']

        try:
            amenities = facade_relation_manager.get_all_amenities_names_from_place(place_id)
            amenities_response = {
                "place_id": place_id,
                "place_amenities": amenities
            }

        except ValueError as e:
            abort(400, str(e))
        
        return amenities_response, 200
    

@api.route('/<string:place_id>/amenities/<string:amenity_name>')
@api.param('place_id', 'The place identifier')
@api.param('amenity_name', 'The amenity name to delete')
class AmenityPlaceDelete(Resource):
    @api.doc('get_all_amenity_names_for_a_place')
    def delete(self, place_id, amenity_name):
        """Delete an amenity from place list"""
        facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
        facade = current_app.extensions['HBNB_FACADE']

        try:
            place = facade.place_facade.get_place(place_id)

        except ValueError as f:
            abort(400, str(f))

        if amenity_name in place["amenities"]:
            try:
                facade_relation_manager.delete_amenity_from_place_list(amenity_name, place_id)
                return {"message": f"Amenity: {amenity_name} has been deleted from the place_amenities list"}, 200
            
            except ValueError as e:
                abort(400, str(e))

        else:
            return {"message": f"Amenity: {amenity_name} not found in the place_amenities list"}, 400
    
 #   <------------------------------------------------------------------------>

@api.route('/<place_id>/reviews')
@api.param('place_id', 'The place identifier')
@api.param('user_id', 'The reviewer identifier')
class ReviewPlaceList(Resource):
    @api.doc('add_review_to_a_place')
    @api.expect(add_review_model)
    @api.marshal_with(add_review_model) # type: ignore
    def post(self, place_id):
        """Create a review for a place"""
        facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
        new_review= request.get_json()
        
        try:
            review = facade_relation_manager.create_review_for_place(place_id, new_review)

        except ValueError as e:
            abort(400, str(e))

        return review, 201
    
    @api.doc('get_all_reviews_for_a_place')
    @api.marshal_with(get_all_reviews_success_model)
    def get(self, place_id):
        """Get all reviews for a place"""
        facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']

        try:
            reviews_list = facade_relation_manager.get_all_reviews_dict_from_place_reviews_id_list(place_id)
            reviews_response = {
                "reviews": reviews_list
            }
        
        except ValueError as e:
            abort(400, str(e))
        
        return reviews_response, 200
    
@api.route('/<string:place_id>/review/<string:review_id>')
@api.param('place_id', 'The place identifier')
@api.param('review_id', 'The review to delete from the place')
class AmenityReviewDelete(Resource):
    @api.doc('delete_a_review_from_a_place')
    def delete(self, place_id, review_id):
        """Delete a review from a place"""
        facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']

        try:
            facade_relation_manager.delete_review_from_place_list(review_id, place_id)
            return {"message": f"Review: {review_id} has been deleted from the place_reviews list"}, 200
        
        except ValueError as e:
            abort(400, str(e))