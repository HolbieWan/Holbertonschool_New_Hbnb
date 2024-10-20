from flask import Blueprint, current_app, jsonify, request, abort

places_bp = Blueprint('places', __name__)


@places_bp.route('/places', methods=["POST"])
def create_place():
    facade = current_app.config['FACADE']
    new_place = request.get_json()
    try:
        place = facade.place_facade.create_place(new_place)

    except ValueError as e:
        abort(400, str(e))

    if place is None:
        abort(400, "Place already exists")
    
    return jsonify(place), 201

 #   <------------------------------------------------------------------------>


@places_bp.route('/places', methods=["GET"])
def get_all_places():
    facade = current_app.config['FACADE']
    places = facade.place_facade.get_all_places()
    return places

 #   <------------------------------------------------------------------------>


@places_bp.route('/places/<place_id>', methods=["GET"])
def get_place(place_id):
    facade = current_app.config['FACADE']
    try:
        place = facade.place_facade.get_place(place_id)
    except ValueError as e:
        abort(404, "e")
    return place

 #   <------------------------------------------------------------------------>

@places_bp.route('/places/<place_id>', methods=["PUT"])
def update_user(place_id):
    facade = current_app.config['FACADE']
    updated_data = request.get_json()
    try:
        updated_place = facade.place_facade.update_place(place_id, updated_data)
    except ValueError as e:
        abort(400, "e")
    return updated_place

 #   <------------------------------------------------------------------------>

@places_bp.route('/places/<place_id>', methods=["DELETE"])
def delete_user(place_id):
    facade = current_app.config['FACADE']
    place = facade.place_facade.get_place(place_id)
    try:
        facade.place_facade.delete_place(place_id)
    except ValueError as e:
        abort(400, "e")
    return (f"Deleted place: {place}")

 #   <------------------------------------------------------------------------>

@places_bp.route('/places/<owner_id>', methods=["GET"])
def get_all_places_by_owner_id(owner_id):
    facade = current_app.config['FACADE']
    try:
        places = facade.place_facade.get_all_places_from_owner_id(owner_id)
    except ValueError as e:
        abort(400, "e")
    return (f"Places of owner: {owner_id}: {places}")