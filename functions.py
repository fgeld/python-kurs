#!/usr/bin/env python3
def say_hi (name):
    print('Hi {}!'.format(name))
say_hi('Jason')
say_hi('everybody')

def say_hello (name1, name2):
    ''' This is a function that displays names'''
    print('Hi {} {}!'.format(name1, name2))
say_hello(name1 = 'Jane', name2 = "John")

help(say_hello)
# help(function_namne) will display the function's description that the pgrogramme should provide in the function

