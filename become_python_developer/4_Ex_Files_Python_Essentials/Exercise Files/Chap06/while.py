#-!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# while loops 

# will loop until the secret word is provided
# secret = 'swordfish'
# pw = ''

# while pw != secret:
#     pw = input("What's the secret word? ")


# Add count (number of attempts)
secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5 


while pw != secret:
	# add counter
	count += 1
	if count > max_attempt:
		break # will break the while loop, will stop
	if count == 3:
		continue # will jump execution and continue on with the next line of code
	pw = input(f"{count}: What's the secret word? ")
else:
	auth = True

print("Authorized" if auth else "Calling the FBI...")
