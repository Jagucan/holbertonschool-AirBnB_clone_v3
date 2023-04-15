#!/usr/bin/python3
""" Index Module """

if __name__ == "__main__":
    from api.v1.views import app_views
    from flask import jsonify, Flask
    from models import storage

    app = Flask(__name__)
    app.register_blueprint(app_views)

    @app_views.route("/api/v1/status")
    def status_route():
        """ app view routes """
        response = jsonify({"status": "OK"})
        return response

    @app_views.route("/api/v1/stats", methods=["GET"])
    def get_stats():
        """ Retrieves the number of each object by type """
        stats = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Review'),
            'states': storage.count('State'),
            'users': storage.count('User')
        }
        return jsonify(stats)

    app.run(host="0.0.0.0", port=5000, debug=True)
