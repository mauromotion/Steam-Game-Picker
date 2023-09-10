# Steam Game Picker

#### Video demo: <url here>

## Description:

_This is my final project for [Harvard's CS50x](https://cs50.harvard.edu/x/2023/)._


Have you hoard too many games on [Steam](https://steamcommunity.com/) during the last few sales? Do you even remember what games are in your library anymore?
Or maybe you feel like playing a game but you can't decide which one because you have too may choices?
The Steam Game Picker will help you choose your next game to play.

Make sure you enter your [correct Steam username](https://www.wikihow.com/See-Your-Account-Name-in-Steam). The app will now load your library.

Now you can choose between a few filters: 
- All your library
- Only the games that you've never played at All
- Only games that you have played before
- Your Top 10 most played games
- Your Top 25 most played games
- Your Top 50 most played games

Then you can click the button and the app will choose a random game between your specified selection.

## Restults page:

Here you can click the title or the thumbnail of the game and get to its Steam page. There is also some useful information about the game here:
- How many hours you've played the game for
- The metacritic score
- The various game's genres

If you don't like the game you can click the green button and try another pick with the same settings you've chosen before.
Or, with the blue button, you can go back to the filters' page and makea different selectoion.
## Technical description:

Steam Game Picker is a web application developed with the [Flask](https://github.com/pallets/flask) frameworkusing a SQLite database.

It fetches data from the Steam API using the [python-steam-api](https://github.com/deivit24/python-steam-api) made by [David Salazar](https://github.com/deivit24).

If you want to try it out on your local machine you'll have to follow a few steps:

- Get your own [Steam API key](https://steamcommunity.com/dev)
- Clone this repository
- Save the key in an .env file in the cloned repository as:
``` STEAM_API_KEY=<YOUR KEY HERE> ```
- Install all the python requirements with:
```python $ pip install -r requirements.txt ```
- Run the Flask application with:
```bash python3 app.py```


