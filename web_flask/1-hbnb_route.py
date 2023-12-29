#!/usr/bin/python3

"""
A script that starts a Flask web application
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


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
