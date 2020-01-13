# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
	# Use the json module to load the string data into a dictionary
	theJSON = json.loads(data)

	# now we can access the contents of the JSON like any other Python object
	if 'title' in theJSON["metadata"]: # checked JSON obj, and title is inside of metadata{} property
		print(theJSON["metadata"]["title"]) # access to metadata{} like a dictionary obj

	
	#---- output the number of events, plus the magnitude and each event name ----

	count = theJSON["metadata"]["count"] # create variable that holds the count of the earthquakes
	print(str(count) + ' events recorded')

	# for each event, print the place where it occurred
	print('\nEvent occurred at:')
	# Iterate through the array of features, then print i sub properties and in particular the place
	for i in theJSON['features']:
		print(i['properties']['place'])
	print('---------------------\n')

	# print the events that only have a magnitude greater than 4
	for i in theJSON['features']:
		if i['properties']['mag'] >= 4.0:
			print("%2.1f" % i['properties']['mag'], i['properties']['place'])

	  
	# print only the events where at least 1 person reported feeling something
	print('\nEvents that were felt:')
	for i in theJSON['features']:
		feltReports = i['properties']['felt']
		if feltReports != None:
			if feltReports >0 :
				print("%2.1f" % i['properties']['mag'], i['properties']['place'], ', reported: ' + str(feltReports) + ' times')


	# print the Magnitude, place, longitude & latitude 
	print('\nCoordinates of each Earthquake, with magnitude above 4.5, and place:')
	for i in theJSON['features']:
		if i['properties']['mag'] > 4.5:
			"""Based on the structure of the JSON file: when printing be aware of:
				> When printing a value inside of dictionary do: ['key']['value']
				> When printing value inside of dictionary, inside of list do: ['key']['value'][index_num]"""
			print("%2.1f" % i['properties']['mag'], i['properties']['place'], i['geometry']['coordinates'][0], i['geometry']['coordinates'][1])

  


def main():
	# define a variable to hold the source URL
	# In this case we'll use the free data feed from the USGS
	# This feed lists all earthquakes for the last day larger than Mag 2.5
	urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

	# Open the URL and read the data
	webUrl = urllib.request.urlopen(urlData)
	print ("result code: " + str(webUrl.getcode()))

	# if connection success, let's print the webUrl data
	if (webUrl.getcode() == 200):
		data = webUrl.read()
		printResults(data)

	else:
		print('Received error, cannot parse results')

if __name__ == "__main__":
	main()
