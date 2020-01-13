# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1):  # countdown from the end of the array
    	# create an inner loop to compare the neighboring elements, then swap them if need it
    	for j in range(i):
    		if dataset[j] > dataset[ j + 1 ]:
    			temp = dataset[j]
    			dataset[j] = dataset[ j + 1 ]
    			dataset[ j + 1 ] = temp

    	print("Current state: ", dataset) # print step by step to see how the list is sorted

    print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
