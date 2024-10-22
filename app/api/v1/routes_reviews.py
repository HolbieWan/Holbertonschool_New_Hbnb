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

@reviews_bp.route('/places/<place_id>/reviews', methods=["GET"])
def get_all_reviews_id_from_place(place_id):
    facade_relation_manager = current_app.extensions['FACADE_RELATION_MANAGER']
    try:
        reviews = facade_relation_manager.get_all_reviews_id_from_place(place_id)
    except ValueError as e:
        abort(400, "e")
    return jsonify(reviews), 200

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
