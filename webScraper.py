from bs4 import BeautifulSoup
import requests
import re 


r  = requests.get("http://library.howard.edu/content.php?pid=257155&sid=2164686")
data = r.text
soup = BeautifulSoup(data)
soup.i.unwrap()
timelineBox = soup.find_all(class_ = "MsoNormal")
for stuff in timelineBox:
	timelineJunk=stuff.find_all("span")
	for junk in timelineJunk:
		print junk.contents
