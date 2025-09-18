num = 11

while num < 50:
    if num % 2 == 0:
        print(str(num) +" is even")
    else:
        print(str(num) +" is odd")
    num += 1

print("Done")

# % is the remainer symbol
# If the remainer is 0, the number is even
# If the remainer is > 0, the number is odd