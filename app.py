import sqlite3
from flask import Flask, session, render_template, request, redirect, flash

from helpers import get_user_data, get_user_library, get_game_data, random_in_list

app = Flask(__name__)
app.secret_key = "99hh%qW&^nqEfjreZi"


# Set up sqlite3 database
def get_db():
    db = sqlite3.connect("library.db")
    return db


def init_db():
    db = get_db()
    db.executescript(open("schema.sql").read())
    db.commit()
    return db


# Select a random game from a list based on a query
def get_random_game(query):
    # Initialize db
    db = get_db()
    c = db.cursor()

    # Count the number of games
    count_me = c.execute(query).fetchall()
    count = len(count_me)

    # Initialize the variables
    name = ""
    playtime = 0
    url = ""
    description = ""
    image = ""
    metacritic = 0
    genres = ""

    # Pick a random number from 1 to the max of the list
    random_pick = random_in_list(count)

    pick = c.execute(query).fetchall()[random_pick - 1]

    # Get data from the picked row
    appid = pick[1]
    name = pick[2]
    playtime = pick[3]

    # Get the rest of the picked game's data from the API
    game_data = get_game_data(appid)

    url = game_data["url"]
    description = game_data["description"]
    image = game_data["image"]
    metacritic = game_data["metacritic"]
    genres = game_data["genres"]

    return name, playtime, url, description, image, metacritic, genres


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        # or get_steam_data(request.form.get('username')) == None:
        if not request.form.get("username") or get_user_data(username) is None:
            flash("Please make sure you have entered a valid username.", "error")
            return render_template("home.html")
        else:
            # Initialize database
            db = init_db()

            # Get user's data and library
            user_data = get_user_data(username)
            user_library = get_user_library(username)

            nickname = user_data["nickname"]
            tot_games = user_data["tot_games"]
            avatar = user_data["avatar"]

            # Store variables into session
            session["username"] = username
            session["nickname"] = nickname
            session["tot_games"] = tot_games
            session["avatar"] = avatar

            # Store user's data into the database
            db.execute(
                "INSERT INTO user (username, nickname, tot_games, avatar)  VALUES (?, ?, ?, ?)",
                (username, nickname, tot_games, avatar),
            )
            db.commit()

            # Loop through each game in library and
            # store them into the database
            for game in user_library:
                appid = game["appid"]
                name = game["name"]
                playtime = round((game["playtime_forever"] / 60), 1)

                db.execute(
                    "INSERT INTO library (appid, name, playtime) VALUES (?, ?, ?)",
                    (appid, name, playtime),
                )

            db.commit()

            return render_template(
                "filters.html", nickname=nickname, tot_games=tot_games, avatar=avatar
            )
    else:
        return render_template("home.html")


@app.route("/filters", methods=["GET", "POST"])
def filters():
    if request.method == "POST":
        # Get the user's input
        filter = request.form.get("filter")
    else:
        # Get data from the session
        filter = session.get("filters")

    # Initialize the variables
    name = ""
    playtime = 0
    url = ""
    description = ""
    image = ""
    metacritic = 0
    genres = ""
    nickname = session.get("nickname")
    avatar = session.get("avatar")
    info_text = ""

    # Logic
    match filter:
        case "any_game":
            query = "SELECT id, appid, name, playtime FROM library"

            (
                name,
                playtime,
                url,
                description,
                image,
                metacritic,
                genres,
            ) = get_random_game(query)
            info_text = "From Your Steam's Library:"
            session["filters"] = "any_game"

        case "never_played":
            query = "SELECT id, appid, name, playtime FROM library WHERE playtime = 0"

            (
                name,
                playtime,
                url,
                description,
                image,
                metacritic,
                genres,
            ) = get_random_game(query)

            info_text = "From Your Never Played Games:"
            session["filters"] = "never_played"

        case "only_played":
            query = "SELECT id, appid, name, playtime FROM library WHERE playtime != 0"

            (
                name,
                playtime,
                url,
                description,
                image,
                metacritic,
                genres,
            ) = get_random_game(query)

            info_text = "From The Games You've Already Played:"
            session["filters"] = "only_played"

        case "top_10":
            query = "SELECT id, appid, name, playtime FROM library ORDER BY playtime DESC LIMIT 10"

            (
                name,
                playtime,
                url,
                description,
                image,
                metacritic,
                genres,
            ) = get_random_game(query)

            info_text = "From Your Top 10 Most Played Games:"
            session["filters"] = "top_10"

        case "top_25":
            query = "SELECT id, appid, name, playtime FROM library ORDER BY playtime DESC LIMIT 25"

            (
                name,
                playtime,
                url,
                description,
                image,
                metacritic,
                genres,
            ) = get_random_game(query)

            info_text = "From Your Top 25 Most Played Games:"
            session["filters"] = "top_25"

        case "top_50":
            query = "SELECT id, appid, name, playtime FROM library ORDER BY playtime DESC LIMIT 50"

            (
                name,
                playtime,
                url,
                description,
                image,
                metacritic,
                genres,
            ) = get_random_game(query)

            info_text = "From Your Top 50 Most Played Games:"
            session["filters"] = "top_50"

        case _:
            print("error")

    return render_template(
        "results.html",
        name=name,
        playtime=playtime,
        url=url,
        description=description,
        image=image,
        metacritic=metacritic,
        genres=genres,
        avatar=avatar,
        nickname=nickname,
        info_text=info_text,
    )


@app.route("/results", methods=["GET", "POST"])
def results():
    # Get data from session
    nickname = session.get("nickname")
    tot_games = session.get("tot_games")
    avatar = session.get("avatar")

    if request.method == "POST":
        # Get the user's input
        if request.form.get("back_to_filters"):
            return render_template(
                "filters.html", avatar=avatar, nickname=nickname, tot_games=tot_games
            )
        else:
            return redirect("/filters")

    else:
        return render_template(
            "results.html", nickname=nickname, tot_games=tot_games, avatar=avatar
        )


if __name__ == "__main__":
    app.run(debug=True)
