import random
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)


# Get data from Steam API
def get_user_data(username):
    try:
        # Fetch user's info
        userinfo = steam.users.search_user(username)

        # Fetch data for the user
        steam_id = userinfo["player"]["steamid"]

        # Check if the username is valid
        # if not isinstance(userinfo['player'], int):
        #     return None

        nickname = userinfo["player"]["personaname"]
        tot_games = steam.users.get_owned_games(steam_id)["game_count"]
        avatar = userinfo["player"]["avatarfull"]

        # Build the usera_data dictionary
        user_data = {"nickname": nickname, "tot_games": tot_games, "avatar": avatar}

        return user_data

    except (KeyError, ValueError, IndexError, TypeError):
        return None


# Get data from Steam API
def get_user_library(username):
    # Fetch user's library
    userinfo = steam.users.search_user(username)
    steam_id = userinfo["player"]["steamid"]
    owned_games = steam.users.get_owned_games(steam_id)["games"]

    return owned_games


# Fetch data for the random game that has been selected
def get_game_data(appid):
    game_data = {}

    # Generate game's URL
    url_base = "https://store.steampowered.com/app/{}"
    url = url_base.format(appid)

    # Fetch the game's description
    try:
        description = steam.apps.get_app_details(appid)[str(appid)]["data"][
            "short_description"
        ]
    except (KeyError, TypeError):
        description = "No description"

    # Fetch the game's image
    try:
        image = steam.apps.get_app_details(appid)[str(appid)]["data"]["header_image"]
    except (KeyError, TypeError):
        image = "No image"

    # Fetch the game's metacritic score
    try:
        metacritic = steam.apps.get_app_details(appid, "US", "metacritic")[str(appid)][
            "data"
        ]["metacritic"]["score"]
    except (KeyError, TypeError):
        metacritic = "No score"

    # Fetch the game's genres
    try:
        get_genres = steam.apps.get_app_details(appid, "US", "genres")[str(appid)][
            "data"
        ]["genres"]

        genres = ""

        for genre in get_genres:
            value = genre["description"]
            genres += value + ", "

        genres = genres[:-2]
    except KeyError:
        genres = "No data"

    # Build the data set
    game_data["url"] = url
    game_data["image"] = image
    game_data["metacritic"] = metacritic
    game_data["genres"] = genres
    game_data["description"] = description

    return game_data


# Generate a random integer between 1 and the argument
def random_in_list(len):
    return random.randrange(1, len)
