#!/usr/bin/python3
''' starts a Flask web application '''
from flask import Flask

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


if __name__ == '__main__':
    ''' main function '''
    app.run(host='0.0.0.0', port=5000)
