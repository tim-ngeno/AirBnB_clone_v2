#!/usr/bin/python3
"""Starting a Flask Web App"""
from flask import Flask, abort, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Displays Hello HBNB! on the URL '/' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Defines the HBNB URL route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Defines the C URL with additional text info"""
    if "_" in text:
        text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route("/python/", defaults={"text": "is cool"},
           strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Defines the python URL with additional text info"""
    if "_" in text:
        text = text.replace("_", " ")
    return "Python {}".format(escape(text))


@app.route("/number/<n>", strict_slashes=False)
def number_route(n):
    """Defines the number route URL"""
    try:
        n = int(n)
        return "{} is a number".format(escape(n))
    except ValueError:
        abort(404)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template_route(n):
    """Defines the number route URL with a template"""
    n = int(n)
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
