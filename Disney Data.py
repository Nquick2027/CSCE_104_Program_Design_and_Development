import requests
# Error? In terminal window (pip install requests)

# We need a custom object that can hold 5 properties
class DisneySong:
    # initializer / custructor
    def __init__(self, rnk, ttl, mov, yea, lyr):
        # Holds the 5 properties listed in the file
        self.rank = rnk
        self.title = ttl
        self.movie = mov
        self.year = yea
        self.lyrics = lyr

response = requests.get('https://raw.githubusercontent.com/hxchua/datadoubleconfirm/master/datasets/DisneySongs25.csv')

# read all the lines from the file, put each in a string
# text_lines is a list of those strings
# (one song per line)
text_lines = response.text.split('\n')

# # How many lines are in the file
# print(len(text_lines))
# # 1 header line, 25 song lines, 1 empty line, lines = 27

# # print just one line:
# print(text_lines[25])
# let_it_go = text_lines[23]

# # Split up that one line by the comma character
# components = let_it_go.split(',', 4)
# # components[0] is '3' (Rank)
# # Components[1] is 'Let it Go' (Title)
# # components[2] is 'Frozen' (Movie)
# # Components[3] is '2013' (Year)
# # Components[4] is 'Lyrics' (Until next comma split) which is not what we want
# # The 4 in split(',', 4) means it stops splitting after 4 commas
# # Componets[4] now becomes "Lyrics" or the rest of the lines
# print(components[2]) # Frozen

song_list = []

# TODO: Process ALL lines in the file
for one_line in text_lines:
    # one_line represents each line in the file, one at a time
    components = one_line.split(',', 4)

    # if removes the blank row
    # The blank row causes an error since it has no "," to split by
    if len(components) > 4:
        rank = components[0]
        title = components[1]
        movie = components[2]
        year = components[3]
        lyrics = components[4]

        song = DisneySong(rank, title, movie, year, lyrics)
        
        # keep a list of songs
        song_list.append(song)

# # AFTER the loop
# print(len(song_list))
# # 26 'songs' in the list
# # 25 are valid, the first one is the header row (pretending to be a song)

# # 3 Options: Delete, Skip, Ignore
# # Option 1: Delete
song_list.pop(0)

# # Option 2: Skip
# for song in song_list[1:]:
#     print(song.title)

# # Option 3: Ignore
# for song in song_list:
#     if song.rank != 'Rank':
#         print(song.title)
# #     #  OR
# for song in song_list:
#     if song.lyrics != 'Lyrics':
#         print(song.title)

# Now we have one list of songs, no header, no empty row
# 25 song objects in a single, clean, list: song_list

print('Here are the best songs in the list:')
for song in song_list:
    if song.movie == 'The Lion King':
        print(song.title)
# Done