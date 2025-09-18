
# Function to add to numbers
# num1 and num2 are called "arguments"
def add_nums(num1, num2):
    return num1 + num2
def sub_nums(num1, num2):
    return num1 - num2
def mult_nums(num1, num2):
    return num1 * num2
def div_nums(num1, num2):
    return num1 / num2
def mod_nums(num1, num2):
    return num1 % num2

# Loop starts here
while True:
    first = int(input("\nEnter the first number: "))
    second = int(input("Enter the second number: "))

    # first and second are called parameters
    print("\nThe sum is: " +str(add_nums(first, second)))

    print("The difference is: " +str(sub_nums(first, second)))
    print("The difference is also: " +str(sub_nums(second, first)))

    print("The product is: " +str(mult_nums(first, second)))

    print("The quotient is: " +str(div_nums(first, second)))
    print("The quotient is also: " +str(div_nums(second, first)))

    print("The modulo is: " +str(mod_nums(first, second)))
    print("The modulo is also: " +str(mod_nums(second, first)))

    u_quit = input("\nDo you want to quit? (y/n): ")

    if u_quit == "y":
        break
# Loop ends here