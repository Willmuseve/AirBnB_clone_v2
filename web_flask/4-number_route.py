#!/usr/bin/python3

"""
A script that starts a a flask web app on 
0.0.0.0, port 5000
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
def c_lang(text):
    """
    Returns text.
    """
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Returns text.
    """
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<int:n>', strict_slashes=False)
def show_num(n):
    """
    Returns param if it is int.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
