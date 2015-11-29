from bs4 import BeautifulSoup
import requests
import re 

r  = requests.get("https://en.wikipedia.org/wiki/Timeline_of_United_States_history#20th_century")
data = r.text
soup = BeautifulSoup(data)

tables = soup.find_all(class_="wikitable");
 
print len(tables)

print tables[4]

# invalid_tags = ['b', 'i', 'u']


# for x in soup.find_all():
# 	if len(x.text) == 0:
# 		x.extract()


# for tag in invalid_tags: 
# 	for match in soup.findAll(tag):
# 		match.replaceWithChildren()

