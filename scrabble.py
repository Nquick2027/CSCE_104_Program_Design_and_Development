# download a file from Github
# Python libaries: math, random, io
# keyword: import
import requests
# Terminal: pip install requests (Windows)
#           pip3 install requests (Mac users)
# HTTP Verbs: GET, PUT, POST, DELETE
# use requests.get to fetch the file from Github
response = requests.get('https://raw.githubusercontent.com/redbo/scrabble/master/dictionary.txt')
# debug: print(response.text)
word_list = response.text.split('\n')
# how many words in the list? 178,691
word_count = len(word_list)
print( word_count )

# read the contents into memory

# count all characters in all words
char_count = 0
# track the longest word
longest_word = ''
# track the shortest word
# if you want to identify a small thing, start with a large thing
shortest_word = 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'

# look at each word, one at a time
#                   reversed = make a copy and reverse the copy
for current_word in reversed(word_list):
# alternative:      word_list.reverse()     # <-- alter the list order
    # current_word represents each word in the list, one at a time
    char_count = char_count + len(current_word)
    # char_count += len(current_word)

    # algorithm for finding the longest word:
    # 1. look at the each word, one at a time
    # 2. if the current word is longer than the longest word we've found
    #    true: current word is now the longest
    #    false: nothing (skip it)
    if len(current_word) > len(longest_word):
        longest_word = current_word
    
    # algorithm for finding the shortest word:
    if len(current_word) < len(shortest_word):
        shortest_word = current_word

# statistical analysis (OUTSIDE the loop)
# longest word, shortest word, and the average length of all words
print('The average length is {}'.format( char_count / word_count ))
print('The longest word is: ' + longest_word)
print('The shortest word is: ' + shortest_word)
