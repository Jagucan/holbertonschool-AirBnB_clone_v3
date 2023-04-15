#!/usr/bin/python3
""" States views module """

if __name__ == "__main__":

    from api.v1.views import app_views
    from flask import jsonify, abort, request
    from models import storage, State

    @app_views.route("/api/v1/states", methods=["GET"])
    def get_all_states():
        """Retrieves the list of all State objects"""
        states = storage.all(State).values()
        list_states = []
        for state in states:
            list_states.append(state.to_dict())
        return jsonify(list_states)

    @app_views.route("/api/v1/states", methods=["POST"])
    def create_a_state():
        """Creates a State object"""
        if not request.is_json:
            abort(400, "Not a JSON")
        req = request.get_json()
        if "name" not in req:
            abort(400, "Missing name")
        state = State(**req)
        storage.new(state)
        storage.save()
        return jsonify(state.to_dict()), 201

    @app_views.route("/api/v1/states/<state_id>", methods=["GET"])
    def get_a_state(state_id):
        """Retrieves a State object"""
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        return jsonify(state.to_dict())

    @app_views.route("/api/v1/states/<state_id>", methods=["DELETE"])
    def delete_a_state(state_id):
        """Deletes a State object"""
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        storage.delete(state)
        storage.save()
        return jsonify({})

    @app_views.route("/api/v1/states/<state_id>", methods=["PUT"])
    def update_a_state(state_id):
        """Updates a State object"""
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        if not request.is_json:
            abort(400, "Not a JSON")
        req = request.get_json()
        for key, value in req.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(state, key, value)
        storage.save()
        return jsonify(state.to_dict())

    app.run(host="0.0.0.0", port=5000, threaded=True)
