#!/usr/bin/python3
""" Cities module """

if __name__ == "__main__":

    from api.v1.views import app_views
    from flask import jsonify, abort, request
    from models import storage, State, City

    @app_views.route("/api/v1/states/<state_id>/cities", methods=["GET"])
    def get_all_cities_by_state(state_id):
        """Retrieves the list of all City objects of a State"""
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        cities = storage.all(City).values()
        list_cities = []
        for city in cities:
            if city.state_id == state_id:
                list_cities.append(city.to_dict())
        return jsonify(list_cities)

    @app_views.route("/api/v1/cities/<city_id>", methods=["GET"])
    def get_city(city_id):
        """Retrieves a City object"""
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        return jsonify(city.to_dict())

    @app_views.route("/api/v1/cities/<city_id>", methods=["DELETE"])
    def delete_city(city_id):
        """Deletes a City object"""
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        storage.delete(city)
        storage.save()
        return jsonify({})

    @app_views.route("/api/v1/states/<state_id>/cities", methods=["POST"])
    def create_city(state_id):
        """Creates a City object"""
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        if not request.is_json:
            abort(400, "Not a JSON")
        req = request.get_json()
        if "name" not in req:
            abort(400, "Missing name")
        city = City(**req)
        city.state_id = state_id
        storage.new(city)
        storage.save()
        return jsonify(city.to_dict()), 201

    @app_views.route("/api/v1/cities/<city_id>", methods=["PUT"])
    def update_city(city_id):
        """Updates a City object"""
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        if not request.is_json:
            abort(400, "Not a JSON")
        req = request.get_json()
        for key, value in req.items():
            if key not in ["id", "state_id", "created_at", "updated_at"]:
                setattr(city, key, value)
        storage.save()
        return jsonify(city.to_dict())

    app.run(host='0.0.0.0', port='5000', threaded=True)
