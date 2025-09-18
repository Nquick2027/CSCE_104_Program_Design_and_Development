import math

print('Welcome to the Calculator Application!')
print('Please enter two numbers to start the calculation:\n')

def add(num1, num2):
    calc = num1 + num2
    result = '{} + {} = {}'.format(num1, num2, calc)
    return result

def subtract(num1, num2):
    calc = num1 - num2
    result = '{} - {} = {}'.format(num1, num2, calc)
    return result

def multiply(num1, num2):
    calc = num1 * num2
    result = '{} * {} = {}'.format(num1, num2, calc)
    return result

def divide(num1, num2):
    calc = num1 / num2
    result = '{} / {} = {}'.format(num1, num2, calc)
    return result

def modulus(num1, num2):
    calc = num1 % num2
    result = '{} % {} = {}'.format(num1, num2, calc)
    return result

def power(num1, num2): 
    calc = pow(num1, num2)
    result = '{} ^ {} = {}'.format(num1, num2, calc)
    return result

def pythagorean(num1, num2):
    calc = math.sqrt(pow(num1, 2) + pow(num2, 2))
    calc2 = pow(num1, 2) + pow(num2, 2)
    result = '{}^2 + {}^2 = {}^2 or {}'.format(num1, num2, calc, calc2)
    return result

def compare(num1, num2):
    if num1 > num2:
        comparison = 'greater than'
    elif num1 < num2:
        comparison = 'less than'
    elif num1 == num2:
        comparison = 'equal to'
    
    result = '{} is {} {}'.format(num1, comparison, num2)
    return result

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    prompt = input('\nEnter the number of the funtion you wish to use: \nAdd(1), \nSubtract(2), \nMultiply(3), \nDivide(4), \nModulus(5), \nPower(6), \nPythagorean(7), \nCompare(8) \nNumber: ')

    print()
    if prompt == '1':
        print(add(num1, num2))
    if prompt == '2':
        print(subtract(num1, num2))
    if prompt == '3':
        print(multiply(num1, num2))
    if prompt == '4':
        print(divide(num1, num2))
    if prompt == '5':
        print(modulus(num1, num2))
    if prompt == '6':
        print(power(num1, num2))
    if prompt == '7':
        print(pythagorean(num1, num2))
    if prompt == '8':
        print(compare(num1, num2))

    end = input('Do you wish to perform another calculation? (Y/N): ')
    if end == 'N' or end == 'n' or end == 'No' or end == 'no':
        print('\nThank you for using this application!')
        break
    print()