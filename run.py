import pandas


def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')


import re
for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid US local phone number')
    else:
        print (test_string, 'rejected')