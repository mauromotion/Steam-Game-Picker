from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)


def get_steam_data(username):

    userinfo = steam.users.search_user(username)
    print(userinfo)

    steam_id = userinfo['player']['steamid']
    print(steam_id)

    owned_games = steam.users.get_owned_games(steam_id)
    print(owned_games)

    terraria = steam.apps.search_games("terraria")
    print(terraria)

    return owned_games


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
'image': image_url,
'url': store_url,
'description': description,
'genres': genres
}

'''
