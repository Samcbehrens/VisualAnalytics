import csv 
import datetime
import json
import calendar


def convertTime(dateAsString):
	MillisecNum=''
	if len(dateAsString)>4:
		conv = datetime.datetime.strptime(dateAsString, '%m/%d/%Y')
		MillisecNum = calendar.timegm(conv.timetuple())
	else:
		numberAsInt = int(dateAsString)
		d = datetime.datetime(numberAsInt,1,1)
		MillisecNum = calendar.timegm(d.timetuple())
	return MillisecNum



def readCsv():

	allInformation = []

	with open('usTimeline.csv', 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
		csvfile.seek(0)
		reader=csv.reader(csvfile,dialect)
		for line in reader:
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
	timeline = {"label": "timeline3", "times": []}
	addEvent={"color":"blue", "label":"description", "starting_time": 1}

	## Must be in a certain format have to put in a array and then a set...crying 
	outerMost = []

	for n in soup:
			if n[1]!='':
				

			if n.isdigit():
				millis = convertTime(n)
				addEvent["starting_time"] = millis
				
			else:
				addEvent["label"] = n	
						
			if addEvent["label"]!="description" and addEvent["starting_time"]!=1:
				randomNum = random.randint(0,4)
				addEvent["color"]=colors[randomNum]
				timeline["times"].append(addEvent)

				addEvent={"color":"blue", "label":"description", "starting_time": 1}
				
	outerMost.append(timeline)
	return outerMost


if __name__ == '__main__':
	allInformation = readCsv()
	newFormation = reformat(allInformation)

	for n in newFormation:	
		print n

