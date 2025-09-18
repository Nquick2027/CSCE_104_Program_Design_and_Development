import random

# There is a library for all of these so you donj't hve to type them all
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specials = ['*', '&', '%', '!', '@', '#', '$', '^', '?', '(', ')', '\'', '\"', '+', ',', '-', '.', '/', '\\', ',', ';', '<', '>', '=', '[', ']', '_', '{', '}', '|', '`', '~']
all_chars = lowers + uppers + nums + specials

while True:

    password = ''
    length = int(input('How many characters?: '))

    for i in range(length):
        rand_char = random.choice(all_chars) 
        password += rand_char

    print(password)

    choice = input('Do you wish to create another password (Y/N)? ')

    if choice == 'N' or choice == 'n' or choice == 'No' or choice == "no":
        print("Thank you for using this password generator! Quiting now.")
        break