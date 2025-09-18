# days_of_the_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# for day in days_of_the_week:
#     # Day acts as the for loop specific variable 
#     # Similiar to using for (int count = 0; count < 10) in Java for loops
#     print(day)

# suits = ['diamonds', 'hearts', 'spades', 'clubs']

# for card in suits:
#     print(card)

# sum = 0
# for i in range(20):
#     print(i)
#     sum += i
#     print('The sum is now: {}'.format(sum))
#     print()

# print('The toal sum is: {}'.format(sum))
# # Summation from 1 to 19 (from 0 to 19)

# # TODO: Challenge: Print the even numbers from 10 - 19

# # Option 1
# for i in range(10,20):
#     if i % 2 == 0:
#         print(i)

# print()

# # Option 2
# for i in range(10, 20, 2):
#     print(i)

# # The "i" variable only exzists in the loop it was created in

# # TODO: Count down from 150 to 100 by 5s

# # Option 1
# for i in range(150, 99, -5):
#     print(i)

# print()

# # Option 2
# for i in reversed(range(100, 151, 5)):
#     # Reverse does exactly what the name says
#     print(i)

message = 'The quick brown fox jumps over the lazy dog'

for word in message.split():
    print(word)

print()

for i in range(len(message)):
    print(message[i])

print()

for i in reversed(range(len(message))):
    print(message[i])