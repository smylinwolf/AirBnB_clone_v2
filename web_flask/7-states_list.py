#!/usr/bin/python3
''' connect flask to storage '''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' lists state in db storage '''
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_db(exception):
    ''' remove SQLAlchemy Session after each request '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
