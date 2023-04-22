#!/usr/bin/python3
""" Index Module """
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    """  """
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def get_stats():
    """  """
    stats = {
        "amenities" : "amenities",
        "cities" : "cities",
        "places" : "places",
        "reviews" : "reviews",
        "states" : "states",
        "users" : "users"
    }

    count_stats = {}
    for key, value in stats.items():
        count_stats[key] = storage.count(value)
    return jsonify(count_stats)
