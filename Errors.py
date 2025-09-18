# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# fraction = num1 / num2
# print('The quotient is {}'.format(fraction))


# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))
# try:
#     fraction = num1 / num2 # <--- possible division by zero
#     print('The quotient is {}'.format(fraction))
# except ZeroDivisionError:
#     print('Cannot divide by zero!')


# num1 = int(input('Enter the first number: '))
# num2 = int(input('Enter the second number: '))

# if num2 == 0:
#     print('Cannot divide by zero!')
# else:
#     fraction = num1 / num2
#     print('The quotient is {}'.format(fraction))


try:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    fraction = num1 / num2
    print('The quotient is {}'.format(fraction))
except ValueError:
    print('Invalid value!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
except NameError:
    print('Num1 or Num2 is invalid!')

# proactive approach
my_list = []
if len(my_list) > 9:
    print('The tenth item in my list is: {}'.format(my_list[9]))
else:
    print('Not enough items in the list!')

# reactive approach
my_list = []
try:
    print('The tenth item in my list is: {}'.format(my_list[9]))
except IndexError:
    print('Not enough items in the list!')

count = 1
while True:
    print(count)
    count += 1

    u_quit = input('Do you wish to quit? (y/n): ')
    if u_quit == 'y':
        break