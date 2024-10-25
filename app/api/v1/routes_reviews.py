from flask import jsonify, abort, request, Blueprint, current_app
from flask_restx import api, Namespace, Resource, fields

reviews_bp = Blueprint('reviews', __name__)
api = Namespace('reviews', description='Reviews operations')

review_model = api.model('Review', {
    'type': fields.String(required=False, description='Type will be given in response', example='review'),
    'id': fields.String(required=False, description='Id will be given in response', example=''),
    'text': fields.String(required=True, description='Text of the review', example='Very nice !'),
    'rating': fields.Integer(required=True, description='Rating from the user for this place', example='4'),
    'place': fields.String(required=True, description='Id of the reviewed place', example='b8bf4d6f-7f4e-4201-ab6e-3b1287c40f46'),
    'user': fields.String(required=True, description='Id of the owner of the place', example='007c0cdd-c2d1-4232-b262-6314522aca45'),
    'created_at': fields.String(required=False, description='Time of creation, given in response', example=''),
    'updated_at': fields.String(required=False, description='Time of update, given in response', example=''),
})

@api.route('/')
class ReviewList(Resource):
    @api.doc('create_review')
    @api.expect(review_model)
    @api.marshal_with(review_model, code=201) # type: ignore
    def post(self):
        """Create a new review"""
        facade = current_app.extensions['HBNB_FACADE']
        new_review = request.get_json()
        try:
            review = facade.review_facade.create_review(new_review)
        except ValueError as e:
            abort(400, "e")
        return review, 201
    
    @api.doc('get_all_reviews')
    @api.marshal_with(review_model, code=201) # type: ignore
    def get(self):
        """Get a lit of all reviews"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            reviews = facade.review_facade.get_all_reviews()
        except ValueError as e:
            abort(400, "e")
        
        return reviews, 200
        
    #   <------------------------------------------------------------------------>

@api.route('/<string:review_id>')
@api.param('review_id', 'The review identifier')
class ReviewResource(Resource):
    @api.doc('get_a_review_by_id')
    @api.marshal_with(review_model)
    def get(self, review_id):
        """Get a review by review_id"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            review = facade.review_facade.get_review(review_id)
        except ValueError as e:
            abort(400, "e")

        return review, 200

    @api.doc('update_review')
    @api.expect(review_model)
    @api.marshal_with(review_model)
    def put(self, review_id):
        """Update a review"""
        facade = current_app.extensions['HBNB_FACADE']
        new_data = request.get_json()

        try:
            review = facade.review_facade.update_review(review_id, new_data)
        except ValueError as e:
            abort(400, "e")

        return review, 201

    @api.doc('create_review')
    @api.marshal_with(review_model)
    def delete(self, review_id):
        """Delete a review"""
        facade = current_app.extensions['HBNB_FACADE']
        review = facade.review_facade.get_review(review_id)

        try:
            facade.review_facade.delete_review(review_id)
        except ValueError as e:
            abort(400, "e")

        return (f"Review: {review} has been deleted.")


    #   <------------------------------------------------------------------------>

@reviews_bp.route('/<place_id>/reviews', methods=["POST"])
def create_reviews_for_place(place_id):
    facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
    new_review= request.get_json()
    
    try:
        review = facade_relation_manager.create_review_for_place(place_id, new_review)

    except ValueError as e:
        abort(400, "e")

    return review, 201
    
    #   <------------------------------------------------------------------------>

@reviews_bp.route('/places/<place_id>/reviews', methods=["GET"])
def get_all_reviews_id_from_place(place_id):
    facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
    try:
        reviews = facade_relation_manager.get_all_reviews_id_from_place(place_id)
    except ValueError as e:
        abort(400, "e")
    return jsonify(reviews), 200

#   <------------------------------------------------------------------------>

@reviews_bp.route('/places/<place_id>/reviews/<review_id>', methods=["DELETE"])
def delete_amenity_from_place_list(place_id, review_id):
    facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']

    try:
        facade_relation_manager.delete_review_from_place_list(review_id, place_id)
    except ValueError as e:
        abort(400, str(e))

    return jsonify({"message": f"Review: {review_id} has been deleted from amenities list"}), 200

 #   <------------------------------------------------------------------------>
