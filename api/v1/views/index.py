#!/usr/bin/python3
""" Index Module """

if __name__ == "__main__":
    from api.v1.views import app_views
    from flask import jsonify

    app = Flask(__name__)
    app.register_blueprint(app_views)

    @app_views.route("/status")
    def status_route():
        """ app view routes """
        return jsonify({"status": "OK"})
        app.run(debug=True)
