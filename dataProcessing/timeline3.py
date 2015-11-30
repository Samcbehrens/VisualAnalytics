from bs4 import BeautifulSoup
import requests
import re 

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
print finalOutput