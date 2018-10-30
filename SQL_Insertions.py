# Standardized file writing
def write_sql(input_list, file_loc):
    insert = f"insert into {file_loc[file_loc.index('/')+1:]} values ("

    output = ""

    for line in input_list:
        output += insert

        for data in line.split(", "):
            output += f"\n\t{data},"

        output = output[:-1] + "\n);\n\n"

        with open(f"output/{file_loc}_Insertions.sql", "w") as output_file:
            output_file.writelines(output[:-2])


# Names of files and output locations
data = [("music_artists", "MusicDB/Artist"),
        ("music_albums", "MusicDB/Album"),
        ("music_songs", "MusicDB/Song"),
        ("movies_series", "MoviesDB/Series"),
        ("movies_movies", "MoviesDB/Movie")
]

# Loops through the data pairs, opens each input file, reads each file into a list of strings where each string is a
# line (besides '\n') of the text file, and passes the list and output location to write_sql()
for pair in data:
    with open(f"input/{pair[0]}.txt", "r") as input_file:
        write_sql(input_file.read().split("\n"), pair[1])
