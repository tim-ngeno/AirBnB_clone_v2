#!/usr/bin/python3
"""Describe states by state id"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import os

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """Display a list of all states in DBStorage"""
    states = storage.all(State)
    sorted_states = sorted(states.values(),
                           key=lambda state: state.name)
    return render_template("9-states.html", states=sorted_states,
                           single_state=None)


@app.route("/states/<id>")
def state_id(id):
    """Display cities of a specific state by ID"""
    states = storage.all(State)
    single_state = None
    for state in states.values():
        if state.id == id:
            single_state = state
            break
    if os.getenv("HBNB_TYPE_STORAGE") != "db" and single_state:
        single_state.cities = single_state.cities()

    return render_template("9-states.html", states=None,
                           single_state=single_state)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database at the end of the request."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
