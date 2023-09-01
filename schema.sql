DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS library;
DROP TABLE IF EXISTS picked_games;

CREATE TABLE user (
  username TEXT PRIMARY KEY NOT NULL,
  nickname TEXT NOT NULL,
  tot_games NUMERIC NOT NULL,
  avatar TEXT NOT NULL
);

CREATE TABLE library (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    appid NUMERIC not NULL,
    name TEXT NOT NULL,
    playtime NUMERIC NOT NULL
);

/* FIXME: I don't need this table, most probably */ 
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

    FOREIGN KEY(appid) REFERENCES library(appid),
    FOREIGN KEY(playtime) REFERENCES library(playtime),
    FOREIGN KEY(name) REFERENCES library(name)
);
