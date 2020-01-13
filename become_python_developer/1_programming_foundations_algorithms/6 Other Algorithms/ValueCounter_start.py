# using a hashtable to count individual items


# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = dict()

# TODO: iterate over each item and increment the count for each one
for item in items:
	# check if item(fruit) exists
	if (item in counter.keys()):
		# just add 1 to the value to the associated key
		counter[item] += 1 
	# if not, initialize the key value with 1
	else:
		counter[item] = 1

# print the results
print(counter.)
