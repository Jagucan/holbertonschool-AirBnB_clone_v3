#!/usr/bin/python3
""" Index Module """

from api.v1.views import app_views
from flask import jsonify, Flask
from models import storage
from sqlalchemy import text


@app_views.route('/status')
def get_status():
    """  """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def get_stats():
    """ Retrieves the number of each object by type """
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
