r1 = range(20)
# Range(20) is equl to Range(0, 20)
print(r1)

r1_list = list(r1)
# Listifies the range to list each number in the list
print(r1_list)

print(list(range(20)))
# This does all of the above in one step

r2 = range(50, 201)
# Range does no include the highest number, but instead goes on lower. Range(20) stops at 19
print(list(r2))

r3_list = list(range(15, 60, 7))
# The third number makes the list count by that number. Starting number +7 until <= highest number
print(r3_list)