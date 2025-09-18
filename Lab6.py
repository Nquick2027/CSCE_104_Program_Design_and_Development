loop = 'y'
while loop == 'y':
    try:
        num1 = float(input('\nEnter the first number: '))
        num2 = float(input('Enter the second number: '))

        if num2 == 0:
            print('Cannot divide by zero!')
        else:
            print('The quotient is: {}'.format(num1/num2))
    except ValueError:
        print('Invalid value!')
    
    loop = input('Would you like to calculate another? (y/n) ')