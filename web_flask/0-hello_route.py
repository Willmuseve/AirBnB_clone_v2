#!/usr/bin/python3

"""
Starting a simple flask application
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def greet_hbnb():
    """
    a function that returns 'Hello HBNB'.
    """
    return render_template("10-hbnb_filters.html")


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0' debug=None)
