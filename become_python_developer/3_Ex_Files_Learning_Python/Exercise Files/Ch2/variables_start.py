# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
# print(f)

# # re-declaring the variable works
# f= 'abc'
# print(f)

# # ERROR: variables of different types cannot be combined
# print('this is a string' + 123)
# print('this is a string ' + str(123))


# Global vs. local variables in functions
def somefunction():
	# declare f as global variable
	global f
	f= 'def'
	print(f)

''' A global variable affects the variable that has same name that are outside of the function.
	To delete a variable simple use 'del' statement, it will delete definition of variable previously declare
'''	

somefunction()
print(f)

del f
print(f)
 