#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Lists
x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))
print('---' * 2)

# change elements in a list
x = [ 1, 2, 3, 4, 5 ]
x[3] = 999 # change value of index 3 for number 999
for i in x:
    print('i is {}'.format(i))
print('---' * 2)

# Tuples
# tuples cannot be mutable
x = ( 6, 7, 8, 9, 0 )
for i in x:
    print('i is {}'.format(i))
print('---' * 2)


# Dictionaries
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# to get the values of each key
for i in x:
    print('i is {}'.format(i))
print('---' * 2)

# to get the key and the values of a dictionary
for k, v in x.items():
    print('K: {}, v: {}'.format(k, v))
print('---' * 2)

# Dictionaries are mutable 
x['three'] = 42
for k, v in x.items():
    print('K: {}, v: {}'.format(k, v))