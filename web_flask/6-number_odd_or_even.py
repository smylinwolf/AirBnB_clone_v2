#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    displays "Hello HBNB!" for route: /
    '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    '''
    displays "HBNB" for route: /hbnb
    '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''
    - displays "C" followed by value of the text variable
    - replaces underscore "_" with a space " "
    '''
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    '''
    - displays "Python" followed by the value of the text
    - replaces underscore "_" with a space " "
    - displays default value if route is /python/
    '''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    '''
    - displays "<n> is a number" only if n is an integer
    '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''
    - displays a HTML page only if n is an integer
    format:
        - "Number: n" inside body tag
    '''
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''
    - - displays a HTML page only if n is an integer
    format:
        - H1 tag: “Number: n is even|odd” inside the tag BODY
    '''
    return render_template('6-number_odd_or_even.html', value=n)


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
