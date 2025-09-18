num = 1
fizzbuzz = 0
fizz = 0
buzz = 0

while num < 101:
    if num % 3 == 0 and num % 5 == 0:
        fizzbuzz += num
    elif num % 3 == 0:
        fizz += num
    elif num % 5 == 0:
        buzz += num
    num += 1

print('The sum of all FIZZ numbers is {}'.format(fizz))
print('The sum of all BUZZ numbers is {}'.format(buzz))
print('The sum of all FIZZBUZZ numbers is {}'.format(fizzbuzz))