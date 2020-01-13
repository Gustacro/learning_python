# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    # the while loop will run as long as the lowerIdx and the upperIdx don;t cruz each other
    while lowerIdx <= upperIdx:
        pass
        # TODO: calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2

        # TODO: if item is found, return the index
        if itemlist[midPt] == item:
            return midPt

        # TODO: otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1


    if lowerIdx > upperIdx: # If the item is not in the list
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
