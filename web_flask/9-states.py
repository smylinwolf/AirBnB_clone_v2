#!/usr/bin/python3
''' connect flask to storage '''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    ''' lists state in db storage '''
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    ''' lists state in db storage '''
    state = None
    for s in storage.all('State').values():
        if s.id == id:
            state = s
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def close_db(exception):
    ''' remove SQLAlchemy Session after each request '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
