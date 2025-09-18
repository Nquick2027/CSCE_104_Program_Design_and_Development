# suits = ['club', 'spades', 'hearts', 'diamonds']
# print(suits)

# print(suits[2])

# suits[2] = '12345Done'
# print(suits[2])
# print(suits)

# months = ['Jan', 'Feb', 'Mar', 'Apr']
# month_num = 2
# print('Month {} is {}'.format(month_num, months[month_num]))
# # First fix
# print('Month {} is {}'.format(month_num, months[month_num - 1]))
# # Second fix
# print('Month {} is {}'.format(month_num + 1, months[month_num]))

song_list = []

while True:
    # TODO: Ask user for song
    u_song = input('Recommend a great song (type q to quit): ')

   # TODO: Ask if they want to quit
    if u_song == 'q' or u_song == 'Q' or u_song == 'quit' or u_song == 'Quit':
        break

    # TODO: Add song to list
    song_list.append(u_song)

# TODO: Print list
print(song_list)