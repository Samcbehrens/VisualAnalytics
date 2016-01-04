import json
from pprint import pprint

with open('unitedstates.json') as data_file:    
    data = json.load(data_file)

#pprint(data)

information = data.get('cities')
finalArray = []
finalJSON={}
largeJSON={}
largeJSON['places']= {} 
largeJSON.get('places')['type']='GeometryCollection'
largeJSON.get('places')['geometries']= []

pprint(largeJSON)

for city in information:

	name = city.get('name')
	print name 
	print 
	newDict = {'type' : 'Point', 'properties':{ 'name':name.split(',')[0]}}
		

	coordinates = city.get('coordinates')
	print coordinates
	splitCoords = coordinates.split(',')
	coordinates = [float(splitCoords[0]), float(splitCoords[1])]
	newDict['coordinates'] = coordinates

	print largeJSON
	largeJSON.get('places').get('geometries').append(newDict)

pprint(largeJSON)



with open('testCity.json', 'w') as outfile:
    json.dump(largeJSON, outfile)




