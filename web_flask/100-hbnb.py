#!/usr/bin/python3
"""HBNB Flask Web Application"""

from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


@app.route("/hbnb")
def hbnb_route():
    """Displays a HTML page like 8-index.html"""
    states = sorted(storage.all(State).values(), key=lambda x:
                    x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x:
                       x.name)
    places = sorted(storage.all(Place).values(), key=lambda x:
                    x.name)
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
