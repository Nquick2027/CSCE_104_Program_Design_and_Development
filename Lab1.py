num1 = 1

while num1 < 101:
    if num1 % 3 == 0 and num1 % 5 == 0:
        print("FIZZBUZZ")
    elif num1 % 3 == 0:
        print("FIZZ")
    elif num1 % 5 == 0:
        print("BUZZ")
    else:
        print(num1) 
    num1 += 1