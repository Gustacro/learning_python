#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


#---------------------- PRINTING STATEMENTS BASED ON THE PYTHON VERSION RUNNING IN YOUR MACHINE---------------#

# pritn value from variable do:
x = 42
print('Hello, World. {}'.format(x))

## PYTHON 2.
x = 12
print( 'Hello World. %d '% x) 

## Python 3.x; 
x = 3.
s = ('Hello, World. {}'.format(x))
print(s)

## Python 3.6 and above, calling the f string method for printing
x = 15
print(f'Hello World. {x}')


