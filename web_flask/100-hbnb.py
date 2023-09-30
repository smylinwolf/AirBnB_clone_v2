#!/usr/bin/python3
''' Includes Place object to application '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    data = {
        'states': storage.all('State').values(),
        'cities': storage.all('City').values(),
        'amenities': storage.all('Amenity').values(),
        'places': storage.all('Place').values()
    }
    return render_template('100-hbnb.html', models=data)


@app.teardown_appcontext
def close_db(exception=None):
    """
    After each request remove the current SQLAlchemy Session:
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
