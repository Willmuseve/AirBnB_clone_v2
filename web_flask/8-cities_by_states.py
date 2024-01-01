#!/usr/bin/python3

"""
A script that starts a Flask web app
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


def get_state_name(state):
    return state.name


@app.route('/cities_by_states', strict_slashes=False)
def list_of_states():
    """
    A function that renders an HTML template.
    """
    states = storage.all(State).values()

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
