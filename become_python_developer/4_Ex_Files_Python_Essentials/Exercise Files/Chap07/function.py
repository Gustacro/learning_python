#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
	x = 5
	kitten(x) # will call the function kitten()
	print(f"in main: x in {x}")

def kitten(a):
	a = 3  
	print('Meow.')
	print(a)

if __name__ == '__main__': main() # will call the default function called main()
