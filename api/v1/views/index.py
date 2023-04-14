#!/usr/bin/python3
""" Index Module """
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status_route():
    """ app view routes """
    return jsonify({"status": "OK"})
