# create an empty list
my_list = []

# append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert a value at the second position
my_list.insert(1, 15)

# extend my_list with another list
my_list.extend([50, 60, 70])

# remove the last element from my_list
my_list.pop()

# sort my_list in ascending order
my_list.sort()

# find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# print the final state of my_list
print("Final list:", my_list)