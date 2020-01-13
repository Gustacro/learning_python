# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # TODO: using the brute force method
    for i in range(0, len(itemlist) - 1):
    	if itemlist[i] > itemlist[i + 1]:
    		return False
    	
    	
    return True

    # Use comprehensive list to do the same as the for LOOP above:
    # all() will return True if all evaluation are true, or False if any evaluation returns false
    # return all(itemlist[i] <= itemlist[i + 1] for i in range(0, len(itemlist) -1))

print(is_sorted(items1))
print(is_sorted(items2))


