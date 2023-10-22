#!/usr/bin/python3
"""Flask Web Application"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list_route():
    """
    Displays a list of states in DBStorage
    """
    states = storage.all(State)
    sorted_states = sorted(states.values(),
                           key=lambda state: state.name)
    print(sorted_states)
    return render_template("7-states_list.html",
                           states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Removes the current SQLAlchemy session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
