#
# Example file for working with functions
#

# define a basic function
def func1():
	print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
	print(arg1," ", arg2)

# function that returns a value
def cube(x):
	return x*x*x

# function with default value for an argument
def power(num, x=1):
	result = 1
	for i in range(x):
		result = result * num
	return result

#function with variable number of arguments
def multi_add(*args): # variable arguments list
	result = 0
	for x in args: 
		result = result + x
	return result


func1() 		# call the function directly 
print(func1()) 	# the function is called inside of the print statement, output is same as first case, but the outer print statement executes and since out function does not return a value. python returns the string of the constant of None
print(func1)	# return the value of the function itself (object) 
func2(10, 20)
print(func2(10, 20))
print(cube(3))
print(power(2))
print(power(2,3))
print(power(x= 3, num = 2))	# no need to call a function with arguments in particular order, just supply the name along with their value
print(multi_add(4,5,10, 6 ))
