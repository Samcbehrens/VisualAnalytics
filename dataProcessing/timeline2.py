from bs4 import BeautifulSoup
import requests
import re 
from timeline3 import convertTime
from timeline3 import webToJson
from timeline3 import convertToFile

def parsePage(url):
	r  = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	invalid_tags = ['b', 'i', 'u', 'em', 'span']

	for tag in invalid_tags: 
	    for match in soup.findAll(tag):
	        match.replaceWithChildren()

	## Finding the timeline 

	timelineParagraph = soup.find(class_ ="paragraph");
	timelineParagraph = str(timelineParagraph)
	timelineParagraph = timelineParagraph.replace("<br/>","-")
	 
	finalOutput= timelineParagraph.split("-")
	print finalOutput


if __name__ == '__main__':
	url ="http://tgmaa.weebly.com/chronology.html"
	parsed = parsePage(url)
	print parsed
	#converted = webToJson(parsed)
	#print converted


