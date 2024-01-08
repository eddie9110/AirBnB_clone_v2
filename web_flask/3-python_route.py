#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """returns the home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB!"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays C"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_(text):
    """displays Python+text"""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
