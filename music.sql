DROP TABLE IF EXISTS artist, album, song;

CREATE TABLE artist (
id INTEGER PRIMARY KEY,
artist_name TEXT
);

CREATE TABLE album (
id INTEGER PRIMARY KEY,
album_name TEXT,
artist_id INTEGER
);

CREATE TABLE song (
id INTEGER PRIMARY KEY,
song_name TEXT,
album_id INTEGER,
track_id INTEGER,
length_sec INTEGER
)