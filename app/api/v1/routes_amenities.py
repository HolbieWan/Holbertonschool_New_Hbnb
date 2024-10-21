from flask import Blueprint, current_app, jsonify, request, abort

amenities_bp = Blueprint('amenities', __name__)


@amenities_bp.route('/amenities', methods=["POST"])
def create_amenity():
    facade = current_app.extensions['HBNB_FACADE']
    new_amenity = request.get_json()
    
    try:
        amenity = facade.amenity_facade.create_amenity(new_amenity)

    except ValueError as e:
        abort(400, "Amenity already exists")

    if amenity is None:
        abort(400, "Amenity already exist")

    return jsonify(amenity), 201

#   <------------------------------------------------------------------------>

@amenities_bp.route('/amenities', methods=["GET"])
def get_all_amenities():
    facade = current_app.extensions['HBNB_FACADE']
    amenities = facade.amenity_facade.get_all_amenities()
    return amenities

#   <------------------------------------------------------------------------>

@amenities_bp.route('/amenities/<amenity_id>', methods=["GET"])
def get_amenity_from_id(amenity_id):
    facade = current_app.extensions['HBNB_FACADE']
    try:
        amenity = facade.amenity_facade.get_amenity(amenity_id)
    except ValueError as e:
        abort(404, "e")
    return amenity

#   <------------------------------------------------------------------------>

@amenities_bp.route('/amenities/<amenity_id>', methods=["PUT"])
def update_amenity(amenity_id):
    facade = current_app.extensions['HBNB_FACADE']
    updated_data = request.get_json()
    try:
        updated_amenity = facade.amenity_facade.update_amenity(amenity_id, updated_data)
    except ValueError as e:
        abort(404, "e")
    return updated_amenity

