from bs4 import BeautifulSoup
import requests
import re 
import json
import pprint
import datetime
import time
import calendar


def convertTime(dateAsString):

	numberAsInt = int(dateAsString)
	d = datetime.datetime(numberAsInt,1,1)
	MillisecNum = calendar.timegm(d.timetuple())
	MillisecNum = MillisecNum * 1000
	return MillisecNum


def parsePage(url):
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)


	invalid_tags = ['b', 'i', 'u', 'ul','li', 'p','em']
	soup = soup.find(id='primary')



	for tag in invalid_tags: 
	 for match in soup.findAll(tag):
	     match.replaceWithChildren()
	    

	for match in soup.findAll('span'):
		match.replaceWith('')

	for match in soup.findAll('div'):
		match.replaceWith('')


	soup = str(soup)
	soup = soup.replace('<strong>', "%")
	soup = soup.replace('</strong>', "%")
	finalOutput = soup.split('%')

	for n in range(0,4):
		finalOutput[n]=""

	return finalOutput

def convertToFile(filename,formatFile):

	with open(filename, 'w') as outfile:
	     json.dump(formatFile, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(formatFile)

def convertToFile(filename,formatFile):

	with open(filename, 'w') as outfile:
	     json.dump(formatFile, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(formatFile)

def webToJson(soup):


	print 'starting this project'

	## formatting to turn into correct json 

	colors = ["red","orange", "yellow", "green", "blue"]
	timeline = {"label": "timeline3", "times": []}
	addEvent={"color":"blue", "description":"description", "starting_time": 1}

	## Must be in a certain format have to put in a array and then a set...crying 
	outerMost = []


	for n in soup:
		if n.find("span")<0 or n.find("div")<0:
			if n.find("\n\n\n") >=0:

				noNs = n.replace("\n\n\n", "")
				addEvent["description"] = noNs

			else:

				if n.find(':')>=0:
					goodNum = n.replace(':','')
					goodNum= goodNum.strip()
					
					if goodNum.isdigit():
						goodNum = convertTime(goodNum)
					addEvent["starting_time"] = goodNum					

			if addEvent["description"]!="description" and addEvent["starting_time"]!=1:
				addEvent["color"]='red'
				timeline["times"].append(addEvent)

				addEvent={"color":"blue", "description":"description", "starting_time": 1}
			

	outerMost.append(timeline)
	return outerMost


if __name__ == '__main__':

	url = "http://herb.ashp.cuny.edu/items/show/1285"

	resultPage = parsePage(url)
	clean = webToJson(resultPage)
	convertToFile('timeline3.json',clean)

