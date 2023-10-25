#!/usr/bin/python3
"""List all cities by their state"""

import os
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_by_states_route():
    """
    Displays a list of cities and states
    """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    for state in sorted_states:
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            state.cities = sorted(state.cities,
                                  key=lambda c: c.name)
        else:
            state.cities = sorted(state.cities(),
                                  key=lambda c: c.name)
    return render_template("8-cities_by_states.html",
                           states=sorted_states)


@app.teardown_appcontext
def teardown_storage(exception):
    """
    Remove current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
