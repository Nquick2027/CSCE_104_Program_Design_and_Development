import requests

class disney_song:
    def __init__(self, rank, title, movie, year, lyrics):
        self.rank = rank
        self.title = title
        self.movie = movie
        self.year = year
        self.lyrics = lyrics

response = requests.get('https://raw.githubusercontent.com/hxchua/datadoubleconfirm/master/datasets/DisneySongs25.csv')
text_lines = response.text.split('\n')

song_list = []
for song_record in text_lines:
    song_details = song_record.split(',', 4)
    if len(song_details) > 4:
        song_rank = song_details[0].strip()
        song_title = song_details[1].strip()
        song_movie = song_details[2].strip()
        song_year = song_details[3].strip()
        song_lyrics = song_details[4].strip()
        new_song = disney_song(song_rank, song_title, song_movie, song_year, song_lyrics)
        song_list.append(new_song)
# song_list is now full
print("Found {} songs in the list".format(len(song_list)))

# NOTE: use these variables to complete the tasks below
longest_lyrics = 0
long_lyr_song = ''
shortest_lyrics = 20000
short_lyr_song = ''
lyr_char_count = 0

# loop through the list
for song in song_list:
    #   TODO: skip the header line (hint: if song.rank == 'rank')
    if song.rank != 'Rank':

        #   TODO: find the SHORTEST lyrics
        if len(song.lyrics) < shortest_lyrics:
            shortest_lyrics = len(song.lyrics)
            short_lyr_song = song.title
        
        #   TODO: find the LONGEST lyrics
        if len(song.lyrics) > longest_lyrics:
            longest_lyrics = len(song.lyrics)
            long_lyr_song = song.title
        
        #   TODO: find the average length of the lyrics
        lyr_char_count += len(song.lyrics)
 # done with the loop

# TODO: print the song title for the longest lyrics
print('The song with the longest lyrics is: {}'.format(long_lyr_song))
# TODO: print the song title for the shortest lyrics
print('The song with the shortest lyrics is: {}'.format(short_lyr_song))
# TODO: print the average length of the lyrics (for all 25 songs)
lyr_char_count = lyr_char_count / 25
print('The average lyric length of all 25 songs is: {} characters'.format(lyr_char_count))