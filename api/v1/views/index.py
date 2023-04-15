#!/usr/bin/python3
""" Index Module """
from flask import jsonify


@app_views.route("/status")
def status_route():
    from api.v1.views import app_views
    """ app view routes """
    return jsonify({"status": "OK"})
