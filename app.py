import sqlite3
from flask import Flask, render_template, g, request

from helpers import get_steam_data

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

# @app.route("/hello")
# def hello_world():
#     return "<p>Steam Random Picker</p>"


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        username = request.form.get('username')
        # or get_steam_data(request.form.get('username')) == None:
        if not request.form.get('username'):
            return render_template('apology.html')
        else:
            games = get_steam_data(username)
            print(games)
            print(username)


@app.route('/filters', methods=['GET', 'POST'])
def filters():
    if request.method == 'POST':
        return render_template('results.html')
    else:
        return render_template('filters.html')


if __name__ == '__main__':
    app.run(debug=True)
