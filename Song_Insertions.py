artist_names = ["Architects", "As I Lay Dying", "Asking Alexandria", "Breaking Benjamin", "Bring Me The Horizon", "Bullet For My Valentine", "Capture", "Chelsea Grin", "Crown the Empire", "A Day to Remember", "Disturbed", "I See Stars", "Linkin Park", "The Lonely Island", "Make Them Suffer", "Memphis May Fire", "Of Mice & Men", "Shinedown", "Skillet", "A Skylit Drive", "Sleeping with Sirens", "Three Days Grace", "Upon a Burning Body", "We Came as Romans"]
album_names = [("All Our Gods Have Abandoned Us", 2016, "46:11"), ("Awakened", 2012, "42:46"), ("Reckless & Relentless", 2011, "42:25")]
song_names = [("Deathwish", "3:53"), ("A Greater Foundation", "3:46"), ("Closure", "3:58")]


def line(input):
    result = "\n\t{},"

    if isinstance(input, str):
        return result.format("\"{}\"".format(input))
    else:
        return result.format(input)


def song(artist_name, album_name, song_name, song_duration, feature=None):
    output = "insert into Song values ("
    output += line(artist_name) + line(album_name) + line(song_name) + line(song_duration) + "\n\tnull"

    if output[len(output) - 1] == ",":
        output = output[:-1]

    output += "\n);\n\n"

    output_file.writelines(output)


output_file = open("output/Song_Insertions.sql", "w")

for i in range(len(song_names)):
    song(artist_names[i], album_names[i][0], song_names[i][0], song_names[i][1])

output_file.close()