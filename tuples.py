#!/usr/bin/env python3
# Tuples
# tuple_name = (item_1, item_2, item_N)
# tuple_name = (item_1, )


# Exercise

airports = [
    ("O’Hare International Airport", 'ORD'),
    ('Los Angeles International Airport', 'LAX'),
    ('Dallas/Fort Worth International Airport', 'DFW'),
    ('Denver International Airport', 'DEN')
]
for (airport, code) in airports:
    print('The code for {} is {}.'.format(airport, code))