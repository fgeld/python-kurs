#!/usr/bin/env python3
# Dictionaies
# dictionary_name = {key_1: value_1, key_N: value_N}
# dictionary_name = {}
# dictionary_name[key]

# Example
contacts = {'Jason': '555-0123', 'Carl': '555-0987'}
jasons_phone = contacts['Jason']
carls_phone = contacts['Carl']

print('Dial {} to call Jason.'.format(jasons_phone))
print('Dial {} to call Carl.'.format(carls_phone))

contacts['Tony'] = ['555-0570', '555-0000']
print(contacts)
print(len(contacts))

del contacts['Jason']
print(contacts)

for number in contacts['Tony']:
    print('Phone: {}'.format(number))


# Exercise
def display_facts(facts):
    """Displays facts"""
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
    print()
facts = {
    'Jason': 'Can fly an airplane.',
    'Jeff': 'Is afraid of clowns.',
    'David': 'Plays the piano.'
}
display_facts(facts)
facts['Jeff'] = 'Is afraid of heights.'
facts['Jill'] = 'Can hula dance.'
display_facts(facts)
