#
# Example file for working with filesystem shell methods
#
import os
from os import path # to get path files
import shutil # to copy and create back-up files
from shutil import make_archive # to work with zip folders
from zipfile import ZipFile # for creating custom file inside of zip folders


def main():
	# make a duplicate of an existing file
	if path.exists("textfile.txt"): # use exists() function to check if file exists
		# get the path to the file in the current directory
		src = path.realpath('textfile.txt')


		# let's make a backup copy by appending "bak" to name
		dst = src + ".bak"

		# Create and copy over the permissions, modification times, and other info
		# shutil.copy(src, dst) # copy() function, only copy the content of the file
		# shutil.copystat(src, dst) # copy over: modification time, other metadata associated w/ file 

		# rename the original file using os module
		# os.rename('textfile.txt', 'newfile.txt') # this would change the original name of the file


		# now put things into a ZIP archive
		root_dir, tail = path.split(src) # get directory path of the full file path
		print(root_dir, '\n', tail) # print the paths directory of root_dir and tail
		# create compress folder
		shutil.make_archive('archive', 'zip', root_dir) # to create the compress folder,  syntax: make_archive("<folder_name>", "<compress_extension>", <file/s_path>)

		""" So all the files on folder (root_dir) were copy inside of the compress folder called 'archive'"""

		# more fine control over ZIP files ; Selecting which files will be added to zip folder
		with ZipFile('testzip.zip', 'w') as newzip: # create new zipfile named testzip.zip, open it for writing access
			# Add the following files to the zip folder
			newzip.write('textfile.txt') 
			newzip.write('textfile.txt.bak')
	  
if __name__ == "__main__":
	main()
