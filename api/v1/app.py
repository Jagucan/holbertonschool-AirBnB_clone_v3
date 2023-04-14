#!/usr/bin/python3
""" API Module """

from flask import Flask
from models import storage
from api.v1.views import app_views
""" imports """


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def shutdown_session():
    """teardown method to shut down"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
