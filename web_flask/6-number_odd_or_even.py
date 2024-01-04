#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB!"""
    return "HBNB!"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays C"""
    return f"C {text}"

@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_(text):
    """displays Python+text""" 
    text = text.replace("_", " ")
    return f'Python + {text}'

@app.route("/number/<int:n>", strict_slashes=False)
def number_(n):
    """n is a number"""
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_temp(n):
    """renders a html tmplate"""
    return render_template('5-number.html', n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_even(n):
    """renders a html tmplate"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
