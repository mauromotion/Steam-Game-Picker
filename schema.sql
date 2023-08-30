CREATE TABLE library (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    appid NUMERIC not NULL,
    name TEXT NOT NULL,
    playtime NUMERIC NOT NULL,

CREATE TABLE picked_games (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    appid NUMERIC not NULL,
    name TEXT NOT NULL,
    playtime NUMERIC NOT NULL,
    image TEXT NOT NULL,
    url TEXT NOT NULL,
    description TEXT NOT NULL,
    metacritic TEXT NOT NULL,
    genres TEXT NOT NULL,
    FOREIGN KEY(appid) REFERENCES library(appid);
    FOREIGN KEY(name) REFERENCES library(name);
)
