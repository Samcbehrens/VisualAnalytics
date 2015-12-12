import datetime
import calendar
import json
import csv

def convertToFile(filename,formatFile):

	with open(filename, 'w') as outfile:
	     json.dump(formatFile, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(formatFile)

def readPopulationData(fileName):
	allInformation = []
	
	with open(fileName, 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
		csvfile.seek(0)
		reader=csv.reader(csvfile,dialect)
		for line in reader:
			print line
			allInformation.append(line)
	return allInformation

def process(allInformation, ArrayOfIndex):
	finalOutput = []
	for n in allInformation:
		addEvent={'GISJOIN': 'fill','YEAR': 'fill','STATE': 'fill','STATEA': 'fill','COUNTY': 'fill','COUNTYA': 'fill','AREANAME': 'fill','POP': 'fill'}
		print n[ArrayOfIndex[0]]
		print n[ArrayOfIndex[1]]
		newPop = int(n[ArrayOfIndex[0]])+int(n[ArrayOfIndex[1]])
		print 
		print newPop
		print 
		final = addEvent
		final['GISJOIN'] = n[0]
		final['YEAR'] = n[1]
		final['STATE'] = n[2]
		final['STATEA'] = n[3]
		final['COUNTY'] = n[4]
		final['COUNTYA'] = n[5]
		final['AREANAME'] = n[6]
		final['POP'] = newPop
		print final
		finalOutput.append(final)
	return finalOutput

if __name__ == '__main__':
	
	fileName= ''
	while fileName!= 'quit':
		fileName = input("Please tell fileName, or enter 'quit': ")
		readInfo = readPopulationData(fileName)
		arrayOfIndex = input('enter Array numbers in Array Format')
		final = process(arrayOfIndex)
		convertToFile(final)
	