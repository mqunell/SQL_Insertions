artist_names = ["Architects", "As I Lay Dying", "Asking Alexandria", "Breaking Benjamin", "Bring Me The Horizon", "Bullet For My Valentine", "Capture", "Chelsea Grin", "Crown the Empire", "A Day to Remember", "Disturbed", "I See Stars", "Linkin Park", "The Lonely Island", "Make Them Suffer", "Memphis May Fire", "Of Mice & Men", "Shinedown", "Skillet", "A Skylit Drive", "Sleeping with Sirens", "Three Days Grace", "Upon a Burning Body", "We Came as Romans"]
album_name = [("All Our Gods Have Abandoned Us", 2016, "46:11"), ("Awakened", 2012, "42:46"), ("Reckless & Relentless", 2011, "42:25")]


def line(input):
    result = "\n\t{},"

    if isinstance(input, str):
        return result.format("\"{}\"".format(input))
    else:
        return result.format(input)


def album(artist_name, album_name, release_year, duration, genre=None):
    output = "insert into Album values ("
    output += line(artist_name) + line(album_name) + line(duration) + "\n\tnull," + line(release_year)

    if output[len(output) - 1] == ",":
        output = output[:-1]

    output += "\n);\n\n"

    output_file.writelines(output)


output_file = open("output/Album_Insertions.sql", "w")

for i in range(len(album_name)):
    album(artist_names[i], album_name[i][0], album_name[i][1], album_name[i][2])

output_file.close()