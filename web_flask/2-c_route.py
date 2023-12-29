#!/usr/bin/python3

"""
A script that starts a Flask web app
listens on 0.0.0.0, port 5000
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns 'Hello HBNB'.
    """
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """
    Returns text.
    """
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
