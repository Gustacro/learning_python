# 
# Example file for retrieving data from the internet
#


# import modules
import urllib.request # provide classes and code to make http requests

# define main function
def main():
	webUrl = urllib.request.urlopen("http://google.com")
	print("result code: " + str(webUrl.getcode())) # the resulted code could be: 200 if everything is OK, 404 if file Not found
	data = webUrl.read() # will read the entire content of the url
	print(data) # print the data in html format

if __name__ == "__main__":
  main()
