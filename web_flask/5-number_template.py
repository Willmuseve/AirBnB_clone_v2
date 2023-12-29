#!/usr/bin/python3

"""
A script tht starts a flask web application on 0.0.0.0
port 5000
"""


from flask import Flask, render_template

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
    t = text.replace('_', ' ')
    return "C " + t


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """
    Returns text.
    """
    t = text.replace('_', ' ')
    return "Python " + t


@app.route('/number/<int:n>', strict_slashes=False)
def show_num(n):
    """
    Returns  param int is number.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_template(n):
    """
    Renders an html_template if n is a number.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
