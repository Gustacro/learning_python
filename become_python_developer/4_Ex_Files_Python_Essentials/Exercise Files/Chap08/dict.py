#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
	# animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
	# 	'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }

	# Same as dictionary above, but better to read and easy interpretation 
	animals = dict(kitten= 'meow', puppy= 'ruff!', lion= 'grrr',
		giraffe= 'I am a giraffe!', dragon= 'rawr')
	 
	# print_dict(animals)

	# use a for LOOP to print the dictionary without calling print_dict() function
	# for k, v in animals.items(): # k represent keys, and v represent values. Use items() to iterate over the dictionary
	# 	print(f'{k}: {v}') 

	# If you want to print one or the other item from the dictionary:
	# for k in animals.keys(): print(k) # To print only the keys : 
	# for v in animals.values(): print(v) # To print only the values:

	# Alteration to the list
	# print(animals['lion']) # print the value of key by calling the key

	# Change the value of a key
	animals['lion'] = "I'm a lion" 
	print(animals['lion'])

	# Add key and value to the list
	animals['monkey'] = 'haha'
	print(animals['monkey'])

	# search for item in dictionary
	print('lion' in )

def print_dict(o):
	# for x in o.items(): print(f'{x}: {o[x]}')

	# Change the for LOOP to make it more readable using the same method as the for LOOP above, if you want to use the print_dict() function
	for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()

#-----------------------------------------------
