#!/usr/bin/python3
"""Flask Web Application"""

import os
from models import storage
from flask import Flask, render_template
from models.amenity import Amenity
from models.city import City
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """
    Display a html file for hbnb filtered content
    """
    states = sorted(storage.all(State).values(),
                    key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda a: a.name)

    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
