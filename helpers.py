import random
from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)


# Get data from Steam API
def get_steam_data(username):

    # Fetch user's info
    userinfo = steam.users.search_user(username)
    steam_id = userinfo['player']['steamid']
    nickname = userinfo['player']['personaname']
    tot_games = steam.users.get_owned_games(steam_id)['game_count']
    avatar = userinfo['player']['avatarfull']
    owned_games = steam.users.get_owned_games(steam_id)['games']

    library = []

    # Build each game's data set
    for game in owned_games:
        new_game = {}

        appid = game['appid']
        url_base = 'https://store.steampowered.com/app/{}'
        url = url_base.format(appid)

        # Fetch the game's description
        try:
            description = steam.apps.get_app_details(
                appid)[str(appid)]['data']['short_description']
        except (KeyError, TypeError):
            description = 'No description'

        # Fetch the game's image
        try:
            image = steam.apps.get_app_details(
                appid)[str(appid)]['data']['header_image']
        except KeyError:
            image = 'No image'

        # Fetch the game's metacritic score
        try:
            metacritic = steam.apps.get_app_details(
                appid)[str(appid)]['data']['metacritic']['score']
        except (KeyError, TypeError):
            metacritic = 'No score'

        # Fetch the game's genres
        # try:
        #     genres = steam.apps.get_app_details(
        #         appid)[str(appid)]['data']['genres']['description']
        # except KeyError:
        #     genres = 'No data'

        # Build the data set
        new_game['appid'] = game['appid']
        new_game['name'] = game['name']
        new_game['url'] = url
        new_game['image'] = image
        new_game['metacritic'] = metacritic
        # new_game['genres'] = genres
        new_game['description'] = description
        new_game['playtime'] = round((game['playtime_forever'] / 60), 1)

        # Add each game to the library
        library.append(new_game)

    # Build the usera_data dictionary
    user_data = {
        'nickname': nickname,
        'tot_games': tot_games,
        'avatar': avatar
    }

    return library, user_data


# Generate a random integer between 1 and the argument
def random_in_list(len):
    return random.randrange(1, len)


'''
Game data from fetch:

{'appid': 570,
 'name': 'Dota 2',
 'playtime_forever': 1578,
 'img_icon_url': '0bbb630d63262dd66d2fdd0f7d37e8661a410075',
 'playtime_windows_forever': 0,
 'playtime_mac_forever': 0,
 'playtime_linux_forever': 0,
 'rtime_last_played': 1458303053,
 'playtime_disconnected': 0}

This is the URL for the image I get from searching a game:
https://cdn.cloudflare.steamstatic.com/steam/apps/105600/capsule_sm_120.jpg?t=1666290860

This instead is the URL for the header image:
https://cdn.cloudflare.steamstatic.com/steam/apps/105600/header.jpg?t=1666290860

I can grab the last 10 digits from the first URL, the app ID,
and recreate the banner URL myself.

Data I need for each game:

Name, playtime, image, store URL, description, genres.

And so I can return something like:

{
'name': name,
'playtime': playtime,
'image': header_image,
'url': store_url,
'description': description,
'genres': genres
}

'''
