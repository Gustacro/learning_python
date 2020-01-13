#
# Read and write files using the built-in Python file methods
#

def main():
	# Open a file for writing and create it if it doesn't exist
	# f = open('textfile.txt', 'w+') # file name and extension, w = writing parameter, + = create file if doesn't exists

	# Open the file for appending text to the end
	# f = open('textfile.txt', 'a') # a = append data to the file

	# Open the file file for reading and printing in console
	f = open('textfile.txt', 'r')

	# write some lines of data to the file
	# for i in range(10):
	# 	f.write("This is line " + str(i) + '\r\n')

	# close the file when done
	# f.close()

	# Open the file back up and read the contents
	if f.mode == 'r':
		contents = f.read()
		print(contents)

	# read the content as an array of individual lines and printing them
	if f.mode == 'r':
		fl = f.readlines()
		for x in fl:
			print(x)
	
if __name__ == "__main__":
  main()
