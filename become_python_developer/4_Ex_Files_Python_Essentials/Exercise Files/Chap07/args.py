#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
	x = ('meow', 'grrr', 'purr', 'hello', 'world') # tuple list
	kitten(*x) # adding an asterisk (*) before the variable, allow the variable to be called as argument list into the function kitten

def kitten(*args): 	# multiple arguments , (*args) represent an argument list. It is a tuple
	if len(args): 	# check of the length greater than 0
		for s in args:
			print(s)
	else: print('Meow.')

if __name__ == '__main__': main()
