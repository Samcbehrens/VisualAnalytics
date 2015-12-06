from bs4 import BeautifulSoup
import requests
import re 


def convertTime(dateAsString):

	numberAsInt = int(dateAsString)
	d = datetime.datetime(numberAsInt,1,1)
	MillisecNum = calendar.timegm(d.timetuple())
	return MillisecNum

def webToJson(soup):


	print 'starting this project'

	## formatting to turn into correct json 

	colors = ["red","orange", "yellow", "green", "blue"]
	timeline = {"label": "timeline3", "times": []}
	addEvent={"color":"blue", "label":"description", "starting_time": 1}

	## Must be in a certain format have to put in a array and then a set...crying 
	outerMost = []


	for n in soup:
		if n.find("span")<0 or n.find("div")<0:
			if n.find("\n\n\n") >=0:

				noNs = n.replace("\n\n\n", "")
				addEvent["label"] = noNs

			else:

				if n.find(':')>=0:
					goodNum = n.replace(':','')
					goodNum= goodNum.strip()
					
					if goodNum.isdigit():
						goodNum = convertTime(goodNum)
					addEvent["starting_time"] = goodNum					

			if addEvent["label"]!="description" and addEvent["starting_time"]!=1:
				randomNum = random.randint(0,4)
				addEvent["color"]=colors[randomNum]
				timeline["times"].append(addEvent)

				addEvent={"color":"blue", "label":"description", "starting_time": 1}
			

	outerMost.append(timeline)
	return outerMost


if __name__ == '__main__':
	r  = requests.get("http://tgmaa.weebly.com/chronology.html")
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
