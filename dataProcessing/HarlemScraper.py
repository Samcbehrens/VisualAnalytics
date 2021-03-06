from bs4 import BeautifulSoup
import requests
import re 


r  = requests.get("http://library.howard.edu/content.php?pid=257155&sid=2164686")
data = r.text
soup = BeautifulSoup(data)
invalid_tags = ['b', 'i', 'u']

for x in soup.find_all():
    if len(x.text) == 0:
        x.extract()

for tag in invalid_tags: 
    for match in soup.findAll(tag):
        match.replaceWithChildren()

timelineBox = soup.find_all(class_ = "MsoNormal")
timeline = []
for stuff in timelineBox:
	timelineJunk=stuff.find_all("span")
	for junk in timelineJunk:
		print junk.contents