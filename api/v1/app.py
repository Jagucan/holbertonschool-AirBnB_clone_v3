#!/usr/bin/python3
"""
Module for the API
"""


if __name__ == "__main__":

    from flask import Flask, jsonify
    from models import storage
    from api.v1.views import app_views

    app = Flask(__name__)
    app.register_blueprint(app_views)

    @app.teardown_appcontext
    def shutdown_session():
        """ Teardown method to shut down """
        storage.close()

    @app.errorhandler("/api/v1/notexist")
    def not_found():
        return jsonify({"error": "Not found"}), 404

    app.run(host="0.0.0.0", port=5000, threaded=True)
