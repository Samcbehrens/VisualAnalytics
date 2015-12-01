from bs4 import BeautifulSoup
import requests
import re 
import json
import random
import pprint

r  = requests.get("http://herb.ashp.cuny.edu/items/show/1285")
data = r.text
soup = BeautifulSoup(data)
print 'gah'
print soup

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



## formatting to turn into correct json 

colors = ["red","orange", "yellow", "green", "blue"]
timeline = {"label": "timeline3", "times": []}
addEvent={"color":"blue", "label":"description", "starting_time": 1, "ending_time": 2}

for n in finalOutput:
	if n.find("span")<0 or n.find("div")<0:
		if n.find("\n\n\n") >=0:

			noNs = n.replace("\n\n\n","")
			addEvent["label"] = noNs
		else:

			if n.find(':')>=0:
				goodNum = n.replace(':','')

				goodNum= goodNum.strip()
				if goodNum.isdigit():
					goodNum = int(goodNum)
				addEvent["starting_time"] = goodNum
			else:
				goodNum= n.strip()
				print 'error'
				print goodNum
				##goodNum = int(goodNum)
				addEvent["starting_time"] = goodNum

		if addEvent["label"]!="description" and addEvent["starting_time"]!=1:
			randomNum = random.randint(0,4)
			addEvent["color"]=colors[randomNum]
			timeline["times"].append(addEvent)

			addEvent={"color":"blue", "label":"description", "starting_time": 1, "end_time": 2}

with open('timeline3.json', 'w') as outfile:
     json.dump(timeline, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(timeline)