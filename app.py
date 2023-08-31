import sqlite3
from flask import Flask, render_template, request

from helpers import get_user_data, get_user_library, get_game_data, random_in_list

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
        # Initialize the database
        db = get_db()
        c = db.cursor()

        # Get the user's input
        filter = request.form.get('filter')

        # Initialize the variables
        name = ''
        playtime = 0
        url = ''
        description = ''
        image = ''
        metacritic = 0
        genres = ''

        # Logic
        match filter:
            case 'any_game':
                count = (c.execute("SELECT COUNT(*) FROM library")
                         ).fetchone()[0]
                random_pick = str(random_in_list(count))
                game_id = c.execute(
                    "SELECT appid, name, playtime FROM library WHERE id = ?", (random_pick,))
                game_row = game_id.fetchall()[0]
                appid = game_row[0]
                name = game_row[1]
                playtime = game_row[2]

                game_data = get_game_data(appid)

                url = game_data['url']
                description = game_data['description']
                image = game_data['image']
                metacritic = game_data['metacritic']
                genres = game_data['genres']

            case 'never_played':
                print('never played')

            case 'top_5':
                print('top 5')

            case 'top_10':
                print('top 10')

            case 'top_20':
                print('top 20')

            case _:
                print('error')

        return render_template('results.html', name=name, playtime=playtime, url=url, description=description, image=image, metacritic=metacritic, genres=genres)
    else:
        return render_template('filters.html')


if __name__ == '__main__':
    app.run(debug=True)
