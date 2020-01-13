# 
# Example file for parsing and processing XML
#
import xml.dom.minidom # for xml file manipulation

def main():
	# use the parse() function to load and parse an XML file
	doc = xml.dom.minidom.parse('samplexml.xml') # beside load and parse the file, it create an in-memory DOM object to manipulate

	# print out the document node and the name of the first child tag. this names are standard names used in the document object model (DOM)
	print(doc.nodeName)
	print(doc.firstChild.tagName) # to print the first child tag in the xml file

	# get a list of XML tags from the document and print each one
	skills = doc.getElementsByTagName('skill')
	print('%d skills: ' % skills.length)
	# iterate through the skills and print them
	for skill in skills:
		print('\t',skill.getAttribute('name'))

	# create a new XML tag and add it into the document
	newSkill = doc.createElement('skill')
	newSkill.setAttribute('name', 'jQuery')
	doc.firstChild.appendChild(newSkill)


	skills = doc.getElementsByTagName('skill')
	print('%d skills: ' % skills.length)
	for skill in skills:
		print('\t',skill.getAttribute('name'))

if __name__ == "__main__":
	main();

