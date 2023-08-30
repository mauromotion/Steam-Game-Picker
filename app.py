import sqlite3
from flask import Flask, render_template, g, request

from helpers import get_user_data, get_user_library

app = Flask(__name__)

# Set up sqlite3 database
DATABASE = './library.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        # or get_steam_data(request.form.get('username')) == None:
        if not request.form.get('username'):
            return render_template('apology.html')
        else:
            user_data = get_user_data(username)
            user_library = get_user_library(username)

            print(user_library)
            print(user_data)

            return render_template('filters.html')
    else:
        return render_template('home.html')


@app.route('/filters', methods=['GET', 'POST'])
def filters():
    if request.method == 'POST':
        return render_template('results.html')
    else:
        return render_template('filters.html')


if __name__ == '__main__':
    app.run(debug=True)
