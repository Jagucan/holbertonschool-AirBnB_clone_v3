#!/usr/bin/python3
""" Amenity module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage, Amenity


@app_views.route("/api/v1/amenities", methods=["GET"])
def get_all_amenities():
    """Retrieves the list of all Amenity objects"""
    amenities = storage.all(Amenity).values()
    list_amenities = []
    for amenity in amenities:
        list_amenities.append(amenity.to_dict())
    return jsonify(list_amenities)


@app_views.route("/api/v1/amenities/<amenity_id>", methods=["GET"])
def get_amenity(amenity_id):
    """Retrieves a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route("/api/v1/amenities/<amenity_id>", methods=["DELETE"])
def delete_amenity(amenity_id):
    """Deletes a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({})


@app_views.route("/api/v1/amenities", methods=["POST"])
def create_amenity():
    """Creates a Amenity object"""
    if not request.is_json:
        abort(400, "Not a JSON")
    req = request.get_json()
    if "name" not in req:
        abort(400, "Missing name")
    amenity = Amenity(**req)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route("/api/v1/amenities/<amenity_id>", methods=["PUT"])
def update_amenity(amenity_id):
    """Updates a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    if not request.is_json:
        abort(400, "Not a JSON")
    req = request.get_json()
    for key, value in req.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict())
