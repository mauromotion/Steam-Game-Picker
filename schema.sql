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

