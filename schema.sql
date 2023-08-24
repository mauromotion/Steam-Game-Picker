CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    playtime NUMERIC NOT NULL,
    image TEXT NOT NULL,
    url TEXT NOT NULL,
    description TEXT,
    genres TEXT;

