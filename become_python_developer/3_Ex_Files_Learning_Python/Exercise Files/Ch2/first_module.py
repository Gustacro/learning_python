
'''
When python runs a file , first even run any code, sets some special variables: __name__ is one of those. So when python run a python file directly it sets __name__ == __main__ 
'''

## print an statement outside of the function called main()
print("This always be running")


# create function called main
def main():
	print("First Module's Name: {}".format(__name__))

# Use conditional -- if __name__ == '__main__'): main().
if __name__ == "__main__":
	main()
	print('run directly')
else: # adding a else statement it will print on the second script  if the module is being running from another file and not running directly  
	print('run from import')


''' check if this file is been directly run it or its imported'''


def add_binary(a,b):
	# return '{0:b}'.format(a+b)
	# or
	# return format(a + b, 'b')
	# or 
	return	bin(a + b)[2::]

print(add_binary(1,1))

