from bs4 import BeautifulSoup
import requests
import re 

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
