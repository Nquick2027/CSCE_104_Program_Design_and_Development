import random

def flip_coin():
    num = random.randint(0, 1)

    if num == 0:
        return 'Coin flip: Tails'
    elif num == 1:
        return 'Coin flip: Heads'

def roll_d6():
    num = random.randint(1, 6)

    return 'D6 roll: {}'.format(num)

def roll_d20():
    num = random.randint(1, 20)

    return 'D20 roll: {}'.format(num)

def pick_card():
    num = random.randint(0, 3)
    suit = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    num2 = random.randint(1, 13)
    value = ['0', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    return 'Your card: {} of {}'.format(suit[num], value[num2])

while True:
    print('\nWelcome to the game center!\nHere are your options:')
    print('\t1) Flip a coin\n\t2) Pick a random playing card')
    print('\t3) Roll a 6-sided dice\n\t4) Roll a 20-sided dice')
    print('\t5) Quit')
    choice = input('What would you like to do? ')

    if choice == '1':
        print(flip_coin())
    elif choice == '2':
        print(pick_card())
    elif choice == '3':
        print(roll_d6())
    elif choice == '4':
        print(roll_d20())
    elif choice == '5':
        break
    else:
        print('Invalid Choice!')
