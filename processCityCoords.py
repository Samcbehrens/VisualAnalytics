import json
from pprint import pprint

with open('unitedstates.json') as data_file:    
    data = json.load(data_file)

#pprint(data)

information = data.get('cities')
finalArray = []
finalJSON={}
largeJSON={}


for city in information:
		coordinates = city.get('coordinates')
		splitCoords = coordinates.split(',')
		coordinates = [splitCoords[0], splitCoords[1]]
		finalJSON['coordinates']= coordinates
		

		name = city.get('name')
		finalJSON['name'] = name.split(',')[0]

		finalArray.append(finalJSON)


largeJSON['cities'] = finalArray

pprint(largeJSON)



with open('testCity.json', 'w') as outfile:
    json.dump(largeJSON, outfile)




