#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Bitwise operator 

# Hexadecimal literal numbers 0a and 02
x = 0x0a 
y = 0x02
z = x & y

# Using f-string, and format controls, these format specifiers, x--> hexadecimal , b --> binary
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}') # format specifier in this case 02x; it has a leading zero (0), giving 2 character string and its in hexadecimal (x)
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}') # format specifier in this case 08b; it has a leading zero (0), giving 8 character string and its in binary (b)
