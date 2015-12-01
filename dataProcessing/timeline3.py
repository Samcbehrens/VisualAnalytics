from bs4 import BeautifulSoup
import requests
import re 
import json
import random
import pprint

r  = requests.get("http://herb.ashp.cuny.edu/items/show/1285")
data = r.text
soup = BeautifulSoup(data)

invalid_tags = ['b', 'i', 'u', 'ul','li', 'p','em']
soup = soup.find(id='primary')

for tag in invalid_tags: 
 for match in soup.findAll(tag):
     match.replaceWithChildren()


soup = str(soup)
soup = soup.replace('<strong>', "-")
soup = soup.replace('</strong>', "-")
finalOutput = soup.split('-')

for n in range(0,4):
	finalOutput[n]=""

print finalOutput
print
print 

## formatting to turn into correct json 

colors = ["red","orange", "yellow", "green", "blue"]
timeline = {"label": "timeline3", "times": []}
addEvent={"color":"blue", "label":"description", "start_time": 1, "end_time": 2}

for n in finalOutput:
	if n.find("span")<0 or n.find("div")<0:
		if n.find("\n\n\n") >=0:
			print n.find("\n\n\n") >=0
			print "in first if" 
			print n 
			print 
			noNs = n.replace("\n\n\n","")
			addEvent["label"] = noNs
		else:
			print "in else"
			print n 
			print 
			if n.find(':')>=0:
				goodNum = n.replace(':','')
				print 'in replacement : else'
				print n
				print 
				addEvent["start_time"] = goodNum
			else:
				addEvent["start_time"] = n

		if addEvent["label"]!="description" and addEvent["start_time"]!=1:
			randomNum = random.randint(0,4)
			addEvent["color"]=colors[randomNum]
			timeline["times"].append(addEvent)
			print "in other if"
			print 
			addEvent={"color":"blue", "label":"description", "start_time": 1, "end_time": 2}

with open('timeline3.txt', 'w') as outfile:
     json.dump(timeline, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(timeline)