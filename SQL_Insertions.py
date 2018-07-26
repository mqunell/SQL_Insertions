# Standard line formatting
def format_line(input):
    result = "\n\t{},"

    if isinstance(input, str) and input != "null":
        return result.format("\"{}\"".format(input))
    else:
        return result.format(input)


# Standard file writing
def write_sql(input_list, file_loc):
    insert = "insert into %s values (" % file_loc[file_loc.index('/')+1:]

    output = ""

    for line in input_list:
        output += insert

        for data in line:
            output += format_line(data)

        output = output[:-1] + "\n);\n\n"

    with open("output/%s_Insertions.sql" % file_loc, "w") as output_file:
        output_file.writelines(output[:-2])


# Generate SQL files

music_artists = [
    ("Architects", 2004, "null"),
    ("As I Lay Dying", 2000, "null"),
    ("Asking Alexandria", 2006, "null"),
    ("Attila", 2005, "null"),
    ("Avenged Sevenfold", 1999, "null"),
    ("Blessthefall", 2004, "null"),
    ("Born of Osiris", 2003, "null"),
    ("Breaking Benjamin", 1999, "null"),
    ("Bring Me The Horizon", 2004, "null"),
    ("Bullet For My Valentine", 1998, "null"),
    ("Capture", 2010, "null"),
    ("Chelsea Grin", 2007, "null"),
    ("Crown the Empire", 2010, "null"),
    ("A Day to Remember", 2003, "null"),
    ("Disturbed", 1994, "null"),
    ("Five Finger Death Punch", 2005, "null"),
    ("For All Those Sleeping", 2007, 2014),
    ("For Today", 2005, 2016),
    ("I See Stars", 2006, "null"),
    ("Issues", 2012, "null"),
    ("Killswitch Engage", 1999, "null"),
    ("Linkin Park", 1996, "null"),
    ("The Lonely Island", 2001, "null"),
    ("Make Them Suffer", 2008, "null"),
    ("Memphis May Fire", 2006, "null"),
    ("Miss May I", 2007, "null"),
    ("Nickelback", 1995, "null"),
    ("Of Mice & Men", 2009, "null"),
    ("Our Last Night", 2004, "null"),
    ("Papa Roach", 1993, "null"),
    ("Parkway Drive", 2003, "null"),
    ("Rise Against", 1999, "null"),
    ("Shinedown", 2001, "null"),
    ("Skillet", 1996, "null"),
    ("A Skylit Drive", 2005, "null"),
    ("Sleeping with Sirens", 2009, "null"),
    ("Slipknot", 1995, "null"),
    ("System of a Down", 1994, "null"),
    ("Three Days Grace", 1997, "null"),
    ("Upon a Burning Body", 2005, "null"),
    ("We Came as Romans", 2005, "null"),
    ("The Word Alive", 2008, "null")
]

movie_series = [("The Dark Knight", 3), ("Deadpool", 2), ("Anchorman", 2), ("MCU", 20), ("Spider-Man", 3), ("DCEU", 5)]

movie_movies = [
    ("Batman Begins", 2005, 3, "2:20", "Action/Adventure", 70, "Christian Bale/Michael Caine/Ken Watanabe", "The Dark Knight", 1, "streaming"),
    ("The Dark Knight", 2008, 3, "2:32", "Action/Crime/Drama", 82, "Christian Bale/Heath Ledger/Aaron Eckhart", "The Dark Knight", 2, "streaming"),
    ("The Dark Knight Rises", 2012, 3, "2:45", "Action/Thriller", 78, "Christian Bale/Tom Hardy/Anne Hathaway","The Dark Knight", 3, "streaming"),
    ("Deadpool", 2016, 4, "1:48", "Action/Adventure/Comedy", 65, "Ryan Reynolds/Morena Baccarin/T.J. Miller", "Deadpool", 1, "dvd/bluray/hdd/streaming"),
    ("Anchorman 2: The Legend Continues", 2013, 3, "1:59", "Comedy", 61, "Will Ferrell/Christina Applegate/Paul Rudd", "Anchorman", 2, "dvd/bluray/hdd"),
    ("Avengers: Age of Ultron", 2015, 3, "2:21", "Action/Adventure/Sci-Fi", 66, "Robert Downey Jr./Chris Evans/Mark Ruffalo", "MCU", 11, "bluray"),
    ("Captain America: Civil War", 2016, 3, "2:27", "Action/Adventure/Sci-Fi", 75, "Chris Evans/Robert Downey Jr./Scarlett Johansson", "MCU", 13, "bluray"),
    ("The Campaign", 2012, 4, "1:25", "Comedy", 50, "Will Ferrell/Zach Galifianakis/Jason Sudeikis", "null", "null", "bluray"),
    ("Due Date", 2010, 4, "1:35", "Comedy/Drama", 51, "Robert Downey Jr./Zach Galifianakis/Michelle Monaghan", "null", "null", "bluray"),
    ("Spider-Man 3", 2007, 3, "2:19", "Action/Adventure/Sci-Fi", 59, "Tobey Maguire/Kirsten Dunst/Topher Grace", "Spider-Man", 3, "bluray"),
    ("Spider-Man: Homecoming", 2017, 3, "2:13", "Action/Adventure/Sci-Fi", 73, "Tom Holland/Michael Keaton/Robert Downey Jr.", "MCU", 16, "dvd/bluray/hdd/streaming"),
    ("Swordfish", 2001, 4, "1:39", "Action/Crime/Thriller", 32, "John Travolta/Hugh Jackman/Halle Berry", "null", "null", "bluray"),
    ("The Benchwarmers", 2006, 3, "1:20", "Comedy/Sport", 25, "David Spade/Jon Heder/Rob Schneider", "null", "null", "dvd"),
    ("Disturbed: M.O.L.", 2002, "null", "2:30", "MusicDB", "null", "Disturbed", "null", "null", "dvd"),
    ("The Bourne Ultimatum", 2007, 3, "1:55", "Action/Mystery/Thriller", 85, "Matt Damon/Edgar Ramirez/Joan Allen", "Bourne", 3, "dvd"),
    ("The Bourne Legacy", 2012, 3, "2:15", "Action/Adventure/Thriller", 61, "Jeremy Renner/Rachel Weisz/Edward Norton", "Bourne", 4, "dvd"),
    ("Inception", 2010, 3, "2:28", "Action/Adventure/Sci-Fi", 74, "Leonardo DiCaprio/Joseph Gordon-Levitt/Ellen Page", "null", "null", "dvd"),
    ("Land of the Lost", 2009, 3, "1:42", "Action/Comedy/Sci-Fi", 32, "Will Ferrell/Danny McBride/Anna Friel", "null", "null", "dvd"),
    ("The Matrix", 1999, 4, "2:16", "Action/Sci-Fi", 73, "Keanu Reeves/Laurence Fishburne/Carrie-Anne Moss", "Matrix", 1, "dvd"),
    ("Matrix Reloaded", 2003, 4, "2:18", "Action/Sci-Fi", 62, "Keanu Reeves/Laurence Fishburne/Carrie-Anne Moss", "Matrix", 2, "dvd"),
    ("Matrix Revolutions", 2003, 4, "2:09", "Action/Sci-Fi", 47, "Keanu Reeves/Laurence Fishburne/Carrie-Anne Moss", "Matrix", 3, "dvd"),
    ("Memento", 2000, 4, "1:53", "Mystery/Thriller", 80, "Guy Pearce/Carrie-Anne Moss/Joe Pantoliano", "null", "null", "dvd"),
    ("Napoleon Dynamite", 2004, 2, "1:36", "Comedy", 64, "Jon Heder/Efren Ramirez/Jon Gries", "null", "null", "dvd"),
    ("Semi-Pro", 2008, 4, "1:31", "Comedy/Sport", 47, "Will Ferrell/Woody Harrelson/Andre Benjamin", "null", "null", "dvd"),
    ("Blades of Glory", 2007, 3, "1:33", "Comedy/Sport", 64, "Will Ferrell/Jon Heder/Amy Poehler", "null", "null", "dvd"),
    ("Step Brothers", 2008, 4, "1:38", "Comedy", 51, "Will Ferrell/John C. Reilly/Mary Steenburgen", "null", "null", "dvd"),
    ("The Other Guys", 2010, 3, "1:47", "Action/Comedy/Crime", 64, "Will Ferrell/Mark Wahlberg/Derek Jetter", "null", "null", "dvd"),
    ("Talladega Nights: The Ballad of Ricky Bobby", 2006, 3, "1:48", "Comedy/Sport", 66, "Will Ferrell/John C. Reilly/Sacha Baron Cohen", "null", "null", "dvd"),
    ("21 Jump Street", 2012, 4, "1:49", "Action/Comedy/Crime", 69, "Jonah Hill/Channing Tatum/Ice Cube", "null", "null", "hdd/streaming"),
    ("22 Jump Street", 2014, 4, "1:52", "Action/Comedy/Crime", 71, "Channing Tatum/Jonah Hill/Ice Cube", "null", "null", "hdd/streaming"),
    ("Batman v Superman: Dawn of Justice", 2016, 3, "2:31", "Action/Adventure/Fantasy", 44, "Ben Affleck/Henry Cavill/Amy Adams", "DCEU", 2, "hdd/streaming"),
    ("Big Hero 6", 2014, 2, "1:42", "Animation/Action/Adventure", 74, "Ryan Potter/Scott Adsit/Jamie Chung", "null", "null", "hdd/streaming")
]

write_sql(music_artists, "MusicDB/Artist")
write_sql(movie_series, "MoviesDB/Series")
write_sql(movie_movies, "MoviesDB/Movie")


# todo: standardize the functions more; almost everything is identical after the data lists
# todo: add music_album and music_song
