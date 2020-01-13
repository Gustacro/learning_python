#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
print(type(x))


#----------------
# Use -f- format only if you have installed python 3.6 or above
a= 8
b= 9
x = f'seven {a} {b}' 
print('x is {}'.format(x))


#----------------
# adding positional arguments '<' '>' to the format function
a= 8
b= 9
x = f'seven {a:<9} {b:>9}'  # add 9 spaces to the left and 9 spaces to the right of the variables
print('x is {}'.format(x))
y = f'seven {a:<09} {b:>09}'  # add 9 spaces to the left and filleting out with 8 zeros because you count the variable number and same with the right side
print('y is {}'.format(y))



# When dealing with decimals it is important to remember that computer calculate number to get precision not to be accurate for lets see how it works
# Case 1:
x = .1 + .1 + .1 - .3 
print('.1 + .1 + .1 - .3 it is precisely equal to: ', x) # this will return the value: 5.551115123125783e-17

# Now lets see how we can get an accurate result for that arithmetical operation
# lets import decimal
from decimal import *

a = Decimal('.1')
b = Decimal('.3')
x = a + a + a - b 
print('.1 + .1 + .1 - .3 it is accurately equal to: ', x) # it will return the value: 0.0

