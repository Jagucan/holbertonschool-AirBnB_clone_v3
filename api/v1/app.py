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
    def teardown_db(exception):
        """closes the storage on teardown"""
        storage.close()

    @app.errorhandler(404)
    def not_found(error):
        """ Teardown method to not found """
        return jsonify({"error": "Not found"}), 404

    app.run(host='0.0.0.0', port='5000', threaded=True)
