from bs4 import BeautifulSoup
import requests
import re 
import json
import random

r  = requests.get("http://herb.ashp.cuny.edu/items/show/1285")
data = r.text
soup = BeautifulSoup(data)

invalid_tags = ['b', 'i', 'u', 'ul','li', 'p']
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

colors = ["red","orange", "yellow", "green", "blue"]
timeline = {"label": "timeline3", "times": []}
addEvent={"color":"blue", "label":"description", "start_time": 1, "end_time": 2}

for n in finalOutput:
	if n.find("\n\n\n") >=0:
		n.replace("\n\n\n","")
		addEvent["label"] = n
	else:
		addEvent["start_time"] = n

	if addEvent["label"]!="description" && addEvent["start_time"] != 1:
		randomNum = random.randint(0,4)
		addEvent["color"]=colors[randomNum]
		timeline["times"].append(addEvent)
		addEvent={"color":"blue", "label":"description", "start_time": 1, "end_time": 2}



