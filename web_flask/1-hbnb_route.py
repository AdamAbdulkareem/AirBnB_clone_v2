#!/usr/bin/python3
"""
1-hbnb_route.py
===============

Description:
------------
This script starts a Flask web application which is
listening on 0.0.0.0 port 5000

Usage:
------
python3 -m 1-hbnb_route.py

"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
