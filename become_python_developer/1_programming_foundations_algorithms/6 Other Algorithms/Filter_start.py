# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hash table to perform a filter
filter_lst = dict()

# TODO: loop over each item and add to the hash table
for item in items:
	filter_lst[item] = 0

# TODO: create a set from the resulting keys in the hash table
result = set(filter_lst.keys())
print(result)