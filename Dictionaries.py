import random

# # creates new empty dictionary
# month_nums = {}

month_nums = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

# u_month = input('Enter the number of a month: ')
# # You must use brackets to get the index of something even though the dictionary uses curly brackets
# print('Your month is {}'.format(month_nums[u_month]))

# num1 = 3
# num2 = 4
# combine = str(num1 + num2)
# print('Month {} is called {}'.format(combine, month_nums[combine]))

month_con = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December',
}

# short_name = input('Enter the short name of the month: ')
# print('The long name of {} is {}'.format(short_name, month_con[short_name]))

# # TODO:
# # Option 1: pick random number, conver to string, look up month
# num = str(random.randint(1, 12))
# print('Month number {} is named {}'.format(num, month_nums[num]))

# # Option 2: pick a random key from the dictionary directly
# # start with dictionary month_con
# # Get all the keys
# # convert to a list
# # use "random.choice()" to pick a random key
# # store that key in "rand_key" variable
# rand_key = random.choice(list(month_con.keys()))
# # first blank is short month name and second blank is long month name
# print('Month {} is also known as {}'.format(rand_key, month_con[rand_key]))

spanish_translate = {}
# everything goes into key-value pairs
# syntax dictionary[key] = value

# add a value
spanish_translate['Hello'] = 'Hola'
spanish_translate["I'm hungery"] = 'Tengo hambre'
spanish_translate['Chair'] = 'Silla'
spanish_translate["To sleep"] = 'Dormir'

print(spanish_translate)

# replace a value
spanish_translate['Hello'] = 'Ciau'

print(spanish_translate)

# remove a value
spanish_translate.pop('Hello')

print(spanish_translate)
