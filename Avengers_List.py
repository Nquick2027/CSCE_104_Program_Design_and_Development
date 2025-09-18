# Creating a list
avengers = ['Iron Man', 'Thor', 'Captain America']
print(avengers)

# Inserting an item at a specific point in the list
avengers.insert(1, 'Spiderman')
avengers.append('Black Widow')
print(avengers)

# Removing items from the list
avengers.remove('Iron Man')
print(avengers)

# Adding items to the end of lists
avengers.append('Iron Man')
print(avengers)

# Removing at a specific position
avengers.pop(2) # Should remove Captain America at index 2
print(avengers)

# Re-adding Captain America at Index 2
avengers.insert(2, 'Captain America')
print(avengers)

# Adding multiple at once (bulk insert)
avengers.extend(['Hulk', 'Ant Man', 'Black Panther'])
print(avengers)

# Sorting the list
avengers.sort()
print(avengers)

# Reverses the order of the  list
avengers.reverse()
print(avengers)