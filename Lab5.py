import random
# TODO: Create a program that allows a user to write flashcards and then test their own knowledge.

# TODO: Start with an empty dictionary
cards = {}

print('Welcome to the Flashcard creator application!\n')


while True:
    # TODO: Ask for a card term (short), then ask for the definition/answer (long)
    term = input('Enter the term: ')
    definition = input('Enter the definition: ')

    # TODO: Store that in the dictionary
    cards[term] = definition

    # TODO: Loop until the user is done entering flashcards
    more = input('Do you wish to create another card? (Y/N): ')
    if more == 'N' or more == 'n' or more == 'No' or more == 'no':
        break

    print('\n')


while True:
    print('\n')
    # TODO: Now test the user: randomly pick a term, show it, and ask “Ready?”
    rand_key = random.choice(list(cards.keys()))
    print('Term: {}'.format(rand_key))
    prompt = input('Ready? ')

    # TODO: When they hit Enter, show the definition.
    print('Definition: {}'.format(cards[rand_key]))

    # TODO: Repeat the testing until the user chooses to quit.
    end = input('Do you wish to continue? (Y/N): ')
    if end == 'N' or end == 'n' or end == 'No' or end == 'no':
        print('\nThank you for using this application!')
        break