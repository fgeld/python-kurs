#!/usr/bin/env python3
# After creating the fike, change the file permission: chmod +x <file-name>
# Now you can execute the python program with ./<file-name>
# Commments in python requires an hashtag in front
print("Hello World") # We can also use comment behind a code / in the same lien as the code
print("and this is a second hello world")
""" Larger comment over several line 
could be done as well"""
x = [1,2]
 
if x == 1:
    print ("x has the value 1")
elif x == 2:
    print("x has the value 2")

print ()

# Variables - are case sensitive
fruit = 'apple'
fruit = "apple"

# Indexing
# string:   a p p l e
# Index:    0 1 2 3 4


# Integrated functions liek print() and len() and input()
fruit = 'Apple'
first_character = fruit[4]
print (first_character)

fruit_len = len(fruit)
print(fruit_len)

fruit2 = "banana"
print(len(fruit2))

print(fruit.lower())

print(fruit2.upper())

print("I "+ "love "+ "Python")

print("-" * 10)

happiness = "happy " * 3
print(happiness)

version = 3
print('I love Python ' + str(version) + '.')

print('I {} Python today.'.format('love'))

print('{} {} {}'.format ('9', '1', '1'))

fruit3 = input('Enter a name of a fruit: ')
print('{} is a lovely fruit.'.format(fruit3))

# String methods
# upper(): returns a copy of the string in uppercase.
# lower(): returns a copy of the string in lowercase.
# format(): returns a formatted version of the string.


# Exersice 1
animal = 'cat'
vegetable = 'brocoli'
mineral = 'gold'
print('Here is an animal, a vegetable, and a mineral.')
print('cat')
print('vegetable')
print('mineral')

# Exersice 2
user_input = input('Please type something and press enter: ')
print('You entered:')
print(user_input)

# Exersice 3
text = input('What would you like the cat to say? ')
text_length = len(text)
print(' {}'.format('_' * text_length))
print(' < {} >'.format(text))
print(' {}'.format('-' * text_length))
print(' /')
print(' /\_/\ /')
print('( o.o )')
print(' > ^ <')


# integer = 42
# float = 4.2

# Convert a string to an integer
quantity_string = '3'
total = int(quantity_string) + 2
print(total)

# Convert a string to a float
quantity_string = '3'
total = float(quantity_string) + 2
print(total)


age = 31
if age >= 35:
    print('H')
elif age >=30:
    print('F')
else:
    pass



def function_name ():
    # Code block

# Execute function
function_name ()


def say_hi (name):
    print('Hi {}!'.format(name))
say_hi('Jason')
say_hi('everybody')