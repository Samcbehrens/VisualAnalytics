import datetime
import json
import calendar
import csv
import random
from timeline3 import convertToFile

def convertTime(dateAsString):
	numberAsInt = int(dateAsString)
	d = datetime.datetime(numberAsInt,1,1)
	MillisecNum = calendar.timegm(d.timetuple())
	MillisecNum = MillisecNum *1000
	return MillisecNum



def readCsv():

	allInformation = []

	with open('blues.csv', 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
		csvfile.seek(0)
		reader=csv.reader(csvfile,dialect)
		for line in reader:
			print line
			allInformation.append(line)
	return allInformation

def webToJSON(soup):
	colors = ["red","orange", "yellow", "green", "blue"]
	timeline = {"label": "blueTimeline", "times": []}
	addEvent={"color":"blue", "description":"description", "starting_time": 1}

	## Must be in a certain format have to put in a array and then a set...crying 
	outerMost = []
	for n in soup:
		millis = convertTime(n[0])
		addEvent["starting_time"] = millis
		addEvent["description"] = n[1]	
		
		if addEvent["description"]!="description" and addEvent["starting_time"]!=1:
			randomNum = random.randint(0,4)
			addEvent["color"]=colors[randomNum]
			timeline["times"].append(addEvent)

			addEvent={"color":"blue", "description":"description", "starting_time": 1}
			
	outerMost.append(timeline)
	return outerMost


if __name__ == '__main__':
	allInformation = readCsv()
	finalFormation = webToJSON(allInformation)
	convertToFile('bluesTimeline.json',finalFormation)