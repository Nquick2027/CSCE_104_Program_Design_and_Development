# NOTE: You may not post any or all of this code online
# NOTE: do not change the imports
import requests

# NOTE: do not change this class
class disney_song:
    def __init__(self, rank, title, movie, year, lyrics):
        self.rank = rank
        self.title = title
        self.movie = movie
        self.year = year
        self.lyrics = lyrics

# NOTE: do not change these lines of code
response = requests.get('https://raw.githubusercontent.com/hxchua/datadoubleconfirm/master/datasets/DisneySongs25.csv')
text_lines = response.text.split('\n')

# NOTE: do not change these lines of code
song_list = []
for song_record in text_lines:
    song_details = ''
    # first, split by double quotes, to isolate the lyrics
    quotes_split = song_record.split("\"")
    # if the lyrics are in quotes, handle them this way
    if len(quotes_split) > 2:
        # first half has rank, title, movie, year (comma-separated)
        first_half = quotes_split[0]
        # second half has the lyrics
        song_lyrics = quotes_split[1].strip()
        # split the first half by commas
        song_details = first_half.split(",")
    else:
        # some entries don't have quotes around the lyrics, so split by comma
        song_details = song_record.split(',')
        if len(song_details) > 4:
            # the lyrics are in the LAST entry
            song_lyrics = song_details[4].strip()
        # no need for "else"- it's the blank row at the bottom
    # now that we have extracted the lyrics, let's get the rest
    if len(song_details) > 3:
        song_rank = song_details[0].strip()
        song_title = song_details[1].strip()
        song_movie = song_details[2].strip()
        song_year = song_details[3].strip()
        new_song = disney_song(song_rank, song_title, song_movie, song_year, song_lyrics)
        song_list.append(new_song)
# song_list is now full
print("Found {} songs in the list".format(len(song_list)-1))
# NOTE: do not change any of the code above this line

# TODO: find the bugs in the code below
# The code below is SUPPOSED to print the longest song, shortest song, 
# and the average lyric length of all songs, but it's broken.
# There are 6 errors below. Find them and fix them.

# TODO: The EXACT output should be (4 lines):
# Found 25 songs in the list
# Longest: Be Our Guest
# Shortest: Some Day My Prince Will Come
# The average char count is 1037.6

# NOTE: you do NOT need to add any try-except code (not necessary)

longest_lyrics = 0
long_lyr_song = ''
shortest_lyrics = 200000000000                      # Error 1: Shortest Lyric number not set
short_lyr_song = ''
lyr_char_count = 0

# loop through the list
for song in song_list:
    if song.rank != 'Rank':                         # Error 2: Didn't remove title line
        # find the SHORTEST lyrics
        if len(song.lyrics) < shortest_lyrics:
            shortest_lyrics = len(song.lyrics)
            short_lyr_song = song.title             # Error 3: Wrong song.###
        # find the LONGEST lyrics
        if len(song.lyrics) > longest_lyrics:       # Error 4: Lesss than instead of greater than
            longest_lyrics = len(song.lyrics)
            long_lyr_song = song.title
        # sum the char count of the lyrics
        lyr_char_count += len(song.lyrics)      # Error 5 & 6: Equals insted of plus equals, and was in if statement for longest lyrics

# NOTE: you do not need to modify any code below this line
# song title for the longest lyrics
print('Longest: {}'.format(long_lyr_song))
# song title for the shorted lyrics
print('Shortest: {}'.format(short_lyr_song))
# average length of the lyrics (for all 25 songs)
print('The average char count is {}'.format(lyr_char_count / 25))
