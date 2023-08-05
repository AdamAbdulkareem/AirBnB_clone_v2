#!/usr/bin/python3
"""
2-c_route.py
============

Description:
------------
This script starts a Flask web application listening on
port 5000
Routes:
    /:         display “Hello HBNB!”
    /hbnb:     display “HBNB”
    /c/<text>: display “C ” followed by the value
               of the text variable

Usage:
------
python3 -m 2-c_route.py
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    return f'C {text.replace("_", " ")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
