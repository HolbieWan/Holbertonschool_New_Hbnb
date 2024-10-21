from flask import jsonify, abort, request, Blueprint, current_app

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/reviews', methods=["POST"])
def create_review():
    facade = current_app.extensions['HBNB_FACADE']
    new_review = request.get_json()
    try:
        review = facade.review_facade.create_review(new_review)
    except ValueError as e:
        abort(400, "e")
    return jsonify(review)

    #   <------------------------------------------------------------------------>

@reviews_bp.route('/reviews', methods=["GET"])
def get_all_reviews():
    facade = current_app.extensions['HBNB_FACADE']
    try:
        reviews = facade.review_facade.get_all_reviews()
    except ValueError as e:
        abort(400, "e")
    return reviews

    #   <------------------------------------------------------------------------>

@reviews_bp.route('/reviews/<review_id>', methods=["GET"])
def get_reviews_from_review_id(review_id):
    facade = current_app.extensions['HBNB_FACADE']
    try:
        review = facade.review_facade.get_review(review_id)
    except ValueError as e:
        abort(400, "e")
    return review

    #   <------------------------------------------------------------------------>

@reviews_bp.route('/reviews/<review_id>', methods=["PUT"])
def update_review(review_id):
    facade = current_app.extensions['HBNB_FACADE']
    new_data = request.get_json()
    try:
        review = facade.review_facade.update_review(review_id, new_data)
    except ValueError as e:
        abort(400, "e")
    return jsonify(review)

    #   <------------------------------------------------------------------------>

@reviews_bp.route('/reviews/<review_id>', methods=["DELETE"])
def delete_review(review_id):
    facade = current_app.extensions['HBNB_FACADE']
    review = facade.review_facade.get_review(review_id)
    try:
        facade.review_facade.delete_review(review_id)
    except ValueError as e:
        abort(400, "e")
    return (f"Review: {review} has been deleted.")