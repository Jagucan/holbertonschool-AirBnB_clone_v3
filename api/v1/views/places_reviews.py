#!/usr/bin/python3
""" Reviews module """
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.review import Review
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    """ place_id -> reviews get """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    """ reviews_id get """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """ reviews_id get delete """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    """ place_id -> reviews post """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'user_id' not in request.get_json():
        abort(400, "Missing user_id")
    user_id = request.get_json()['user_id']
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if 'text' not in request.get_json():
        abort(400, "Missing text")
    data = request.get_json()
    data['place_id'] = place_id
    review = Review(**data)
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201

@app_views.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    """  reviews_id put """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
