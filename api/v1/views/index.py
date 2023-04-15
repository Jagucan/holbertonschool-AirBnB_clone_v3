#!/usr/bin/python3
""" Index Module """

if __name__ == "__main__":
    from api.v1.views import app_views
    from flask import jsonify, Flask

    app = Flask(__name__)
    app.register_blueprint(app_views)

    @app_views.route("/status")
    def status_route():
        """ app view routes """
        response = jsonify({"status": "OK"})
        response.headers["Content-Type"] = "application/json"
    return response

    app.run(host="0.0.0.0", port=5000, debug=True)
