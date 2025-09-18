import random

print('Welcome to the Flashcard creator application!\n')

def build_deck():
    # TODO: Use a new dictionary every time
    new_deck = {}
    file_name = input('Enter the name of the dictionary: ')

    while True:
        term = input('Enter the term: ')
        definition = input('Enter the definition: ')

        new_deck[term] = definition

        more = input('Do you wish to create another card? (Y/N): ')
        if more == 'N' or more == 'n' or more == 'No' or more == 'no':
            break

    # TODO: Save cards to a file, name file [subject].txt
    with open('{}.txt'.format(file_name), 'w') as file:
        file.write( str(new_deck) )
        print('\nFile saved for subject: ' + file_name)

def quiz_time():
    saved_deck = {}
    print('\nTime for a quiz!\n')

    # TODO: ask the user for the subject name
    file = input('Enter the name of the subject file (casing matters, don\'t add the txt): ') + '.txt'

    # TODO: open [subject].txt, read dictionary, reconstruct it
    with open(file, 'r') as saved_file:
        contents = saved_file.read()
        saved_deck = eval(contents)

    # TODO: use that dictionary instead of flash cards


    while True:
        print('\n')
        term, definition = random.choice(list(saved_deck.items()))
        print('Term: {}'.format(term))
        prompt = input('Ready for the definition? ')

        print('Definition: {}'.format(definition))

        end = input('Do you wish to continue the quiz? (Y/N): ')
        if end == 'N' or end == 'n' or end == 'No' or end == 'no':
            break

# # TODO: Ask the user of they wish to build a new deck or quiz on an existing deck

while True:
    choice = input('(1) Build a new deck, (2) Open an existing deck: ')
    if choice == '1':
        build_deck()
    elif choice == '2':
        quiz_time()
    else:
        print('Invalid Option!')

    repeat = input('Do yo wish to continue using this application? (Y/N): ')
    if repeat == 'N' or repeat == 'n' or repeat == 'No' or repeat == 'no':
            print('\nThank you for using this application!')
            break