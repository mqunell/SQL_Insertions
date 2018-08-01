# Standardized file writing
def write_sql(input_list, file_loc):
    insert = "insert into %s values (" % file_loc[file_loc.index('/')+1:]

    output = ""

    for line in input_list:
        output += insert

        for data in line.split(", "):
            output += "\n\t%s," % data

        output = output[:-1] + "\n);\n\n"

        with open("output/%s_Insertions.sql" % file_loc, "w") as output_file:
            output_file.writelines(output[:-2])


# Read the data into lists of strings where each string is a line (besides '\n') of the text file
with open("input/music_artists.txt", "r") as input_file:
    music_artists = input_file.read().split("\n")

with open("input/music_albums.txt", "r") as input_file:
    music_albums = input_file.read().split("\n")

with open("input/music_songs.txt", "r") as input_file:
    music_songs = input_file.read().split("\n")

with open("input/movies_series.txt", "r") as input_file:
    movies_series = input_file.read().split("\n")

with open("input/movies_movies.txt", "r") as input_file:
    movies_movies = input_file.read().split("\n")


# Generate SQL files
write_sql(music_artists, "MusicDB/Artist")
write_sql(music_albums, "MusicDB/Album")
write_sql(music_songs, "MusicDB/Song")
write_sql(movies_series, "MoviesDB/Series")
write_sql(movies_movies, "MoviesDB/Movie")
