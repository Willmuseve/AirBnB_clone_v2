#!/usr/bin/python3

"""
A script that starts Flask web app
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

def get_state_name(state):
    return state.name

def list_states():
    """
     Displays an HTML page with a list of all State objects in DBStorage.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
