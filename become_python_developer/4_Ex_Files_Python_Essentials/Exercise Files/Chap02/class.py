#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


"""
> Class is definition of an object of an instance of a class.
> Function inside of a class is called method, regular method.
> Variables inside of a class are called class variables 
"""

# Define Class
class Duck:
	# define class variables
	sound = 'Quaaaaaaack!!!'
	walking = 'Walking like a duck.'


	# Regular method or Class method
	def quack(self): # always in a method is the first argument is 'self', and it's reference to the object when the class is used to create an object
		print(self.sound)

	def walk(self):
		print(self.walking)

def main():
	# variable 'donald' assigned from the class. so that makes 'donald' and object of the class Duck
	# use the variable 'donald' to call the class methods quack and the method walk
	donald = Duck()
	donald.quack()
	donald.walk()

if __name__ == '__main__': main()
