#!/usr/bin/python3

"""
A scripts that starts a flask web app
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


def get_state_name(state):
    return state.name


@app.route('/states', strict_slashes=False)
def list_of_states():
    """
    A function that renders an HTML template
    """
    states = storage.all(State).values()

    return render_template('9-states.html', states=states, city=False)


@app.route('/states/<uuid:id>', strict_slashes=False)
def states_and_cities():
    """
    A function that renders an HTML template
    """
    states = storage.all(State).values()

    if id:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', state=state, city=True)
        return render_template('9-states.html', city=False, not_found=True)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
