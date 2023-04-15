#!/usr/bin/python3
""" Index Module """

if __name__ == "__main__":
    from api.v1.views import app_views
    from flask import jsonify

    app = Flask(__name__)

    @app_views.route("/status")
    def status_route():
        """ app view routes """
        return jsonify({"status": "OK"})

    app.run(host="0.0.0.0", port=5000, debug=True)
