# use recursion to implement a countdown counter


def countdown(x):
	# function ends only when value is equal to zero
    if x == 0:
    	print('Done!')
    	return
    # If x not equal to zero, print the x value and re-call the function where (x-1)
    # Sample: x = 5, where (x-1) = 4, and 4 it becomes the new x value 
    else:
    	print(x,"...")
    	countdown(x-1)



countdown(5)
