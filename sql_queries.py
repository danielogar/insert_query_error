# DROP TABLES

songplay_table_drop = ("DROP table if exists songplays")
user_table_drop = ("DROP table if exists users")
song_table_drop = ("DROP table if exists songs")
artist_table_drop = ("DROP table if exists artists")
time_table_drop = ("DROP table if exists time")

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id int, start_time int, user_id int, level text, song_id int, artist_id varchar, session_id int, location varchar, user_agent varchar);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int, first_name text, last_name text, gender text, level text);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar, title text, artist_id varchar, year int, duration float);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar, name text, location text, latitude float, longitude float);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time int, hour int, day int, week int, month int, year int, weekday text);
""")

# INSERT RECORDS

songplay_table_insert = (""" 
""")

user_table_insert = ("""
""")

song_table_insert = "INSERT INTO songs (song_id,title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (0) DO NOTHING;"

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]