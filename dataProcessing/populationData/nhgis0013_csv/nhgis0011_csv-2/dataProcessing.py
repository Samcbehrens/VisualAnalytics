import datetime
import calendar
import json
import csv
import pprint


def findCountyId(StateA, CountyA):
    stateA = stateA.rstrip("0")
    print stateA
    if countyA[-1] == '0':
          countyA = countyA[0:-1]
	print countyA
	final=stateA+countyA
	return final

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
		print 'contents of population in file'
		print n[ArrayOfIndex[0]]
		num1 = n[ArrayOfIndex[0]]
		print 'contents of population in file'
		print n[ArrayOfIndex[1]]
		num2 = n[ArrayOfIndex[1]]
		
		print num1.isdigit()
		print num2.isdigit()

		
		if num1.isdigit(): 
			print "in if"
			num1 = int(n[ArrayOfIndex[0]])
			print num1
			print 
		else:
			print "el"
			num1 = 0
		if num2.isdigit():
			print "in if"
			print num2
			num2 = int(n[ArrayOfIndex[1]])	
		else:
			print "in if"
			num2 = 0


		print "num1"
		print num1 

		print "num2"
		print num2


		newPop = num1 + num2
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
		newPop = 0
		print final
		finalOutput.append(final)
	return finalOutput

if __name__ == '__main__':

	#fileName= 
	#while fileName!= 'quit':

	fileName = "nhgis0011_ds31_1900_county.csv"
	arrayOfIndex = [9,10]
	outputName = "Pop1900.json"

	#fileName = input("Please tell fileName, or enter 'quit': ")
	readInfo = readPopulationData(fileName)

	#arrayOfIndex = input('enter Array numbers in Array Format')
	final = process(readInfo, arrayOfIndex)

	#outputName = input("Please tell what to save it as")
	convertToFile(outputName,final)
	