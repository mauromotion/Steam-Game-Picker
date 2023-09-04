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
            # TODO: either make the apology template or implement the flash alert
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
                # Count the number of rowws/games in the resulting slice of db
                count = (c.execute("SELECT COUNT(*) FROM library")
                         ).fetchone()[0]

                # Pick a random number from 1 to the max of the list
                random_pick = (random_in_list(count))

                pick = c.execute(
                    "SELECT * FROM library").fetchall()[random_pick - 1]

                # Get data from the picked row
                appid = pick[1]
                name = pick[2]
                playtime = pick[3]

                # Get the rest of the picked game's data from the API
                game_data = get_game_data(appid)

                url = game_data['url']
                description = game_data['description']
                image = game_data['image']
                metacritic = game_data['metacritic']
                genres = game_data['genres']

            case 'never_played':
                # Count the number of rowws/games in the resulting slice of db
                count = (c.execute("SELECT COUNT(*) FROM library WHERE playtime = 0")
                         ).fetchone()[0]

                # Pick a random number from 1 to the max of the list
                random_pick = (random_in_list(count))

                pick = c.execute(
                    "SELECT * FROM library WHERE playtime = 0").fetchall()[random_pick - 1]

                # Get data from the picked row
                appid = pick[1]
                name = pick[2]
                playtime = pick[3]

                # Get the rest of the picked game's data from the API
                game_data = get_game_data(appid)

                url = game_data['url']
                description = game_data['description']
                image = game_data['image']
                metacritic = game_data['metacritic']
                genres = game_data['genres']

            case 'only_played':
                # Count the number of rowws/games in the resulting slice of db
                count = (c.execute("SELECT COUNT(*) FROM library WHERE playtime != 0")
                         ).fetchone()[0]

                # Pick a random number from 1 to the max of the list
                random_pick = (random_in_list(count))

                pick = c.execute(
                    "SELECT * FROM library WHERE playtime != 0").fetchall()[random_pick - 1]

                # Get data from the picked row
                appid = pick[1]
                name = pick[2]
                playtime = pick[3]

                # Get the rest of the picked game's data from the API
                game_data = get_game_data(appid)

                url = game_data['url']
                description = game_data['description']
                image = game_data['image']
                metacritic = game_data['metacritic']
                genres = game_data['genres']

            case 'top_5':
                # Count the number of rowws/games in the resulting slice of db
                count = 5

                # Pick a random number from 1 to the max of the list
                random_pick = (random_in_list(count))

                pick = c.execute(
                    "SELECT * FROM library ORDER BY playtime DESC LIMIT 5").fetchall()[random_pick - 1]

                # Get data from the picked row
                appid = pick[1]
                name = pick[2]
                playtime = pick[3]

                # Get the rest of the picked game's data from the API
                game_data = get_game_data(appid)

                url = game_data['url']
                description = game_data['description']
                image = game_data['image']
                metacritic = game_data['metacritic']
                genres = game_data['genres']

            case 'top_10':
                # Count the number of rowws/games in the resulting slice of db
                count = 10

                # Pick a random number from 1 to the max of the list
                random_pick = (random_in_list(count))

                pick = c.execute(
                    "SELECT * FROM library ORDER BY playtime DESC LIMIT 10").fetchall()[random_pick - 1]

                # Get data from the picked row
                appid = pick[1]
                name = pick[2]
                playtime = pick[3]

                # Get the rest of the picked game's data from the API
                game_data = get_game_data(appid)

                url = game_data['url']
                description = game_data['description']
                image = game_data['image']
                metacritic = game_data['metacritic']
                genres = game_data['genres']

            case 'top_20':
                # Count the number of rowws/games in the resulting slice of db
                count = 20

                # Pick a random number from 1 to the max of the list
                random_pick = (random_in_list(count))

                pick = c.execute(
                    "SELECT * FROM library ORDER BY playtime DESC LIMIT 20").fetchall()[random_pick - 1]

                # Get data from the picked row
                appid = pick[1]
                name = pick[2]
                playtime = pick[3]

                # Get the rest of the picked game's data from the API
                game_data = get_game_data(appid)

                url = game_data['url']
                description = game_data['description']
                image = game_data['image']
                metacritic = game_data['metacritic']
                genres = game_data['genres']

            case _:
                print('error')

        return render_template('results.html', name=name, playtime=playtime, url=url, description=description, image=image, metacritic=metacritic, genres=genres)
    else:
        return render_template('filters.html')


if __name__ == '__main__':
    app.run(debug=True)
