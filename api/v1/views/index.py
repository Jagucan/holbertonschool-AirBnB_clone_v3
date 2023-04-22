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
    stats = {}
    stats["amenities"] = storage.count()
    stats["cities"] = storage.count()
    stats["places"] = storage.count()
    stats["reviews"] = storage.count()
    stats["states"] = storage.count()
    stats["users"] = storage.count()
    return jsonify(stats)
