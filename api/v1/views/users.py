#!/usr/bin/python3
""" Module Users """

from flask import abort, jsonify, request
from datetime import datetime
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'])
def get_users():
    """ user get """
    users = User.all()
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict)


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """  user_id get """
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ user_id delete """
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'])
def create_user():
    """ user post """
    if not request.json:
        abort(400, 'Not a JSON')
    if 'email' not in request.json:
        abort(400, 'Missing email')
    if 'password' not in request.json:
        abort(400, 'Missing password')
    user_dict = request.get_json()
    user_dict['created_at'] = datetime.now()
    user_dict['updated_at'] = datetime.now()
    user = User(**user_dict)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """ user_id put """
    user = User.get(user_id)
    if user is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    user_dict = request.get_json()
    user_dict.pop('id', None)
    user_dict.pop('email', None)
    user_dict.pop('created_at', None)
    user_dict.pop('updated_at', None)
    for key, value in user_dict.items():
        setattr(user, key, value)
    user.updated_at = datetime.now()
    user.save()
    return jsonify(user.to_dict()), 200
