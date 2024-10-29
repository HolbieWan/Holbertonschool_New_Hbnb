from flask import jsonify, abort, request, Blueprint, current_app
from flask_restx import api, Namespace, Resource, fields

reviews_bp = Blueprint('reviews', __name__)
api = Namespace('reviews', description='Reviews operations')

review_model = api.model('Review', {
    'type': fields.String(required=False, description='Type will be given in response', example='review'),
    'id': fields.String(required=False, description='Id will be given in response', example=''),
    'text': fields.String(required=True, description='Text of the review', example='Very nice !'),
    'rating': fields.Integer(required=True, description='Rating from the user for this place', example='4'),
    'place_id': fields.String(required=True, description='Id of the reviewed place', example='b8bf4d6f-7f4e-4201-ab6e-3b1287c40f46'),
    'place_name': fields.String(required=False, description='Name of the reviewed place', example='Chez Johnny'),
    'user_id': fields.String(required=True, description='Id of the owner of the place', example='007c0cdd-c2d1-4232-b262-6314522aca45'),
    'user_first_name': fields.String(required=False, description='First_name of the reviewer ', example='Johnny'),
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
        new_review_data = request.get_json()
        try:
            review = facade.review_facade.create_review(new_review_data)
        except ValueError as e:
            abort(400, str(e))
        return review, 201
    
    @api.doc('get_all_reviews')
    @api.marshal_with(review_model, code=201) # type: ignore
    def get(self):
        """Get a list of all reviews"""
        facade = current_app.extensions['HBNB_FACADE']
        try:
            reviews = facade.review_facade.get_all_reviews()
            if not reviews:
                raise ValueError("No review found")
        except ValueError as e:
            abort(400, str(e))
        
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
            abort(400, str(e))

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
            abort(400, str(e))

        return review, 201

    @api.doc('create_review')
    def delete(self, review_id):
        """Delete a review"""
        facade = current_app.extensions['HBNB_FACADE']

        try:
            review = facade.review_facade.get_review(review_id)
            facade.review_facade.delete_review(review_id)
        except ValueError as e:
            abort(400, str(e))

        return (f"Review: {review} has been deleted.")

