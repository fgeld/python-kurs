#!/usr/bin/env python3

# This file explains lists in Python.

animals = ['man', 'bear', 'pig']
# the next line will add a sinlge item at the end of the list
animals.append('cow')
print(animals)

# the next line will add multiple items at the end of the list
more_animals = ['horse', 'dog']
animals.extend(more_animals)
print(animals)

animals.insert(0, 'horse')
print(animals)


some_animals = animals[1:4]
print('Some animals:    {}'.format(some_animals))

bear_index = animals.index('bear')
print(bear_index)


# Looping through a list
# for item_variable in list_name
#       code block

for animal in animals:
    print(animal.upper())

# While loop
index = 0
while index < len(animals):
    print(animals[index])
    index += 1

print(len(animals))

# Ranges
for number in range(1, 10, 2):
    print(number)



