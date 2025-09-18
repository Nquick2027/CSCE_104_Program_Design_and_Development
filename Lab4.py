num1 = 1

# Class version of the function
# def fizzbuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FIZZBUZZ"
#     elif num % 3 == 0:
#         return "FIZZ"
#     elif num % 5 == 0:
#         return "BUZZ"
#     else:
#         return str(num)

# while num1 < 101:
#     print(fizzbuzz(num1))
#     num1 += 1

# print()

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

print()

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i) 
    i += 1