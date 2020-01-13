# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[: mid]
        rightarr = dataset[mid :]

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)


        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                # dataset[k] is single merge array that we're building back up, so it gets the smaller array value between leftarr[i] and rightarr[j]
                dataset[k] = leftarr[i] 
                i += 1  # increment that pointer

            else:
                dataset[k] = rightarr[j]
                j += 1 # increment that pointer
            k += 1

        # TODO: if the left array still has values, add them 
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1 # move index to the next one
            k += 1 # move index to the next one


        # TODO: if the right array still has values, add them
        while j < len(leftarr):
            dataset[k] = rightarr[j]
            j += 1 # move index to the next one
            k += 1 # move index to the next one



# test the merge sort with data
print(items)
mergesort(items)
print(items)
