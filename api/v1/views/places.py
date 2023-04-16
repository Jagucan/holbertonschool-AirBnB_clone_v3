#!/usr/bin/python3
""" Index Module """

if __name__ == '__main__':

    from flask import jsonify, abort, request
    from api.v1.views import app_views
    from models import storage, City, Place, User

    @app_views.route('/cities/<city_id>/places', methods=['GET'])
    def get_places_by_city(city_id):
        """  """
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        places = [place.to_dict() for place in city.places]
        return jsonify(places)

    @app_views.route('/places/<place_id>', methods=['GET'])
    def get_place(place_id):
        """  """
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        return jsonify(place.to_dict())

    @app_views.route('/places/<place_id>', methods=['DELETE'])
    def delete_place(place_id):
        """  """
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        storage.delete(place)
        storage.save()
        return jsonify({})

    @app_views.route('/cities/<city_id>/places', methods=['POST'])
    def create_place(city_id):
        """  """
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        req_json = request.get_json()
        if not req_json:
            abort(400, 'Not a JSON')
        user_id = req_json.get('user_id')
        if not user_id:
            abort(400, 'Missing user_id')
        user = storage.get(User, user_id)
        if user is None:
            abort(404)
        name = req_json.get('name')
        if not name:
            abort(400, 'Missing name')
        place = Place(name=name, user_id=user_id, city_id=city_id)
        storage.new(place)
        storage.save()
        return jsonify(place.to_dict()), 201

    @app_views.route('/places/<place_id>', methods=['PUT'])
    def update_place(place_id):
        """  """
        place = storage.get(Place, place_id)
        if place is None:
            abort(404)
        req_json = request.get_json()
        if not req_json:
            abort(400, 'Not a JSON')
        ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
        for key, value in req_json.items():
            if key not in ignore:
                setattr(place, key, value)
        storage.save()
        return jsonify(place.to_dict())

    app.run(host='0.0.0.0', port='5000', threaded=True)
