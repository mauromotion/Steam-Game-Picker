from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")

steam = Steam(KEY)

# arguments: steamid
user = steam.users.get_user_details("_glennz")

print(user)
