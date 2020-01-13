# 
# Example file for parsing and processing HTML
#
# import modules:
from html.parser import HTMLParser


# global variable:
metacount = 0

# Define class:
class MyHTMLParser(HTMLParser):
	def handle_comment(self, data):
		print('Encountered comment: ', data)		
		pos = self.getpos() # getpos(), returns 2 things; line number and a character position in data where, in this where the comment was encountered.
		print('\tAt line: ', pos[0], 'position ', pos[1])

	def handle_starttag(self, tag, attrs):
		# declare global variables inside of the function
		global metacount
		# count number of meta tags in the file
		if tag == 'meta':
			metacount += 1

		print('Encountered tag: ', tag)		
		pos = self.getpos() # getpos(), returns 2 things; line number and a character position in data where, in this where the comment was encountered.
		print('\tAt line: ', pos[0], 'position ', pos[1])
		
		# print any attributes that the tag has on it.  Note: Remember in HTML only start tag can have attributes, attributes are passed in the attrs argument
		if attrs.__len__() > 0:
			print("\tAttributes:")
			# loop through all attributes
			for a in attrs:
				print("\t", a[0], '=', a[1])

	def handle_endtag(self, tag):
		print('Encountered tag: ', tag)		
		pos = self.getpos() # getpos(), returns 2 things; line number and a character position in data where, in this where the comment was encountered.
		print('\tAt line: ', pos[0], 'position ', pos[1])

	# define function to encounter data:
	def handle_data(self, data):
		if data.isspace():
			return
		print('Encountered data: ', data)		
		pos = self.getpos() # getpos(), returns 2 things; line number and a character position in data where, in this where the comment was encountered.
		print('\tAt line: ', pos[0], 'position ', pos[1]) # print the line and position of the encountered data


def main():
	# instantiate the parser and feed it some HTML
	parser = MyHTMLParser()
	f = open('samplehtml.html') # open html file
	if f.mode == 'r': # check if html file is open to read, meaning that was successfully opened
		contents = f.read() # define variable that contain the html data
		parser.feed(contents) 
		""" passing contents to feed function, takes html and run through line by line, for each time encounters specific kind of data like comments, tags, text data, 
			is going to call functions that you override in your sub-class
			"""
		print("All meta tags found: " + str(metacount))

if __name__ == "__main__":
	main();
