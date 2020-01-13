
# Using recursion to implement power and factorial functions

#Power of means: 2^4 = 2 x 2 x 2 x 2 = 32
def power(num, pwr):
    if pwr == 0:
    	return 1

    else:
    	return num * power(num, pwr-1)



# Factorial of a number: 5! = 5 x 4 x 3 x 2 x 1 = 120
# Special case 0! = 1
def factorial(num):
    if num == 0:
    	return 1

    else:
    	return num * factorial(num - 1)



print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))
 