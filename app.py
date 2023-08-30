import sqlite3
from flask import Flask, render_template, request

from helpers import get_user_data, get_user_library

app = Flask(__name__)


# Set up sqlite3 database
def get_db():
    db = sqlite3.connect('library.db')
    return db


def init_db():
    db = get_db()
    db.executescript(open('schema.sql').read())
    db.commit()
    return db


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        username = request.form.get('username')
        # or get_steam_data(request.form.get('username')) == None:
        if not request.form.get('username'):
            return render_template('apology.html')
        else:
            db = init_db()

            user_data = get_user_data(username)
            user_library = get_user_library(username)

            nickname = user_data['nickname']
            tot_games = user_data['tot_games']
            avatar = user_data['avatar']

            db.execute("INSERT INTO user (username, nickname, tot_games, avatar)  VALUES (?, ?, ?, ?)",
                       (username, nickname, tot_games, avatar))
            db.commit()

            for game in user_library:
                appid = game['appid']
                name = game['name']
                playtime = round(
                    (game['playtime_forever'] / 60), 1)

                db.execute(
                    "INSERT INTO library (appid, name, playtime) VALUES (?, ?, ?)", (appid, name, playtime))

            db.commit()

            return render_template('filters.html', nickname=nickname, tot_games=tot_games, avatar=avatar)
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
