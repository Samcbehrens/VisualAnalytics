from bs4 import BeautifulSoup
import requests
import re 
from timeline3 import convertTime
from timeline3 import webToJson
from timeline3 import convertToFile
import random

## have to parse each page differently because of formatting >:(
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
	print 'timelineParagraph'
	print timelineParagraph
	 
	#finalOutput= timelineParagraph.split("-", ' -', ' - ', '- ')
	finalOutput = re.split(' - |-| -|- ',timelineParagraph)
	print 'output'
	print finalOutput
	return finalOutput

## the parse breaks up the dates in diffrent ways so also have to modify this basic code to adapt to it
def webToJson(soup):

	print 'starting this project'
	print soup
	## formatting to turn into correct json 

	colors = ["red","orange", "yellow", "green", "blue"]
	timeline = {"label": "timeline3", "times": []}
	addEvent={"color":"blue", "label":"description", "starting_time": 1}

	## Must be in a certain format have to put in a array and then a set...crying 
	outerMost = []


	for n in soup:
		#cleanNum = n.strip(' ')
		print 'on line'+n
		print type(n)
		print n
		print n.isdigit()
		if n.isdigit():
			addEvent["starting_time"] = n
			print 'in if'+n
		else:
			addEvent["label"] = n	
			print 'in else'+n			

		print
		if addEvent["label"]!="description" and addEvent["starting_time"]!=1:
			randomNum = random.randint(0,4)
			addEvent["color"]=colors[randomNum]
			timeline["times"].append(addEvent)

			addEvent={"color":"blue", "label":"description", "starting_time": 1}
			

	outerMost.append(timeline)
	print 'in function and got this json'
	print outerMost
	return outerMost

if __name__ == '__main__':
	url ="http://tgmaa.weebly.com/chronology.html"
	parsed = parsePage(url)
	converted = webToJson(parsed)
	# print converted
	


