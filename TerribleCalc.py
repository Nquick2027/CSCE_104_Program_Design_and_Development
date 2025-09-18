# The pound sign acts as a comment in in Python like the /" in Java

print()

# name = input("Enter your name: ")

# print('Hello, ' +name)

# Single and double quotes are the same thing and both act as a string

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

#print(type(num1))
#print(type(num2))

# num1 and num2 are strings
# Convert num1 and num2 to integers

num1 = int(num1)
num2 = int(num2)

# Python can change variales from one form to another
# What is done above is called overriding

# This is how to do it in one line: num1 = int(input("Enter the first number: "))

print("The sum is: " +str(num1 + num2))

# Could also make a second variabel that does the math and then stringify that new variable

print("The difference is: " +str(num1 - num2))
print("The difference is also: " +str(num2 - num1))

print("The product is: " +str(num1 * num2))

print("The quotient is: " +str(num1 / num2))
print("The quotient is also: " +str(num2 / num1))

print()