import csv 
import datetime
import json
import calendar
from timeline3 import convertToFile


def convertTime(dateAsString):
	MillisecNum=''
	conv =''
	if len(dateAsString)>4:
		conv = datetime.datetime.strptime(dateAsString, '%m/%d/%Y')
		MillisecNum = calendar.timegm(conv.timetuple())
	else:
		numberAsInt = int(dateAsString)
		d = datetime.datetime(numberAsInt,1,1)
		MillisecNum = calendar.timegm(d.timetuple())
		
	MillisecNum = MillisecNum *1000
	return MillisecNum




def readCsv():

	allInformation = []

	with open('usTimeline.csv', 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
		csvfile.seek(0)
		reader=csv.reader(csvfile,dialect)
		for line in reader:
			print line
			allInformation.append(line)
	return allInformation

def reformat(allInformation):

	newFormation =[]

	for i in range(0, len(allInformation)):

		## get index out of range if you dont check this first
		if i+1 < len(allInformation)-1:
			##look ahead to see if the next one doesnt have a date
			if allInformation[i+1][0]=='':
				allInformation[i+1][0]=allInformation[i][0]

		#add if it has the correct date
		thisPotYear = allInformation[i][0]
		if thisPotYear.isdigit():
			newFormation.append(allInformation[i])
	return newFormation

def webToJson(soup):

	## formatting to turn into correct json 

	colors = ["red","orange", "yellow", "green", "blue"]
	timeline = {"label": "usTimeline", "times": []}
	addEvent={"color":"blue", "description":"description", "starting_time": 1}

	## Must be in a certain format have to put in a array and then a set...crying 
	outerMost = []
	print soup
	for n in soup:
			print n
			print type(n)
			if n[1] != '':
				print n[1]
				millis = convertTime(n[1])
				addEvent["starting_time"] = millis

			if n[0].isdigit():
				millis = convertTime(n[0])
				addEvent["starting_time"] = millis
				 
	
			addEvent["description"] = n[2]	
			
			if addEvent["description"]!="description" and addEvent["starting_time"]!=1:
				addEvent["color"]='orange'
				print 'addingEvent'
				print addEvent
				timeline["times"].append(addEvent)

				addEvent={"color":"blue", "description":"description", "starting_time": 1}
				
	outerMost.append(timeline)
	return outerMost


if __name__ == '__main__':
	allInformation = readCsv()
	newFormation = reformat(allInformation)
	finalFormation = webToJson(newFormation)
	convertToFile('usTimeline.json',finalFormation)


