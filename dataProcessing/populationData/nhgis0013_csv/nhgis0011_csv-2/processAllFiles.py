import datetime
import calendar
import json
import csv
import pprint

def convertToCSV(outputFileName, contents):
	f = open(outputFileName, 'wt')
	try:
		writer = csv.writer(f)
		writer.writerow( 'state', 'id', 'county', 'areaname', '1900', '1910','1920','1930','1940', '1950','1960','1970') )
		for county in contents :
			writer.writerow( (county['STATE'], county['ID'], county['COUNTY'], county['AREANAME'], county['POP10'],county['POP20'],county['POP30'],county['POP40'],county['POP50'],county['POP60'],county['POP70']))
	except:
		print "problem"
	finally:
		f.close()



def findCountyId(StateA, CountyA):
	modState=''
	modCounty=''
	if CountyA[-1] == '0':
		modState = StateA[0:-1]
	if CountyA[-1] == '0':
		modCounty = CountyA[0:-1]

	final = modState+modCounty


	final = final.lstrip('0')

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

def compileAllDates(DateDictionary):
	allCounties = []
	template = {'STATE': 'fill', "ID" : "fill" ,'COUNTY': 'fill','AREANAME': 'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	
	

def process(allInformation, ArrayOfIndex):
	finalOutput = []
	for n in allInformation:
		addEvent={'YEAR': 'fill', 'STATE': 'fill', "ID" : "fill" ,'COUNTY': 'fill','AREANAME': 'fill','POP': 'fill'}
		
		newPop = 0
		if len(arrayOfIndex)>1:
			num1 = n[ArrayOfIndex[0]]
			num2 = n[ArrayOfIndex[1]]
			if num1.isdigit(): 
				
				num1 = int(n[ArrayOfIndex[0]])
			
			else:
				
				num1 = 0
			if num2.isdigit():
				num2 = int(n[ArrayOfIndex[1]])	
			else:
				num2 = 0

			newPop = num1 + num2
		else:
			newPop = arrayOfIndex[0]

		final = addEvent
		final['YEAR'] = n[1]
		final['STATE'] = n[2]

		final['ID'] = findCountyId(n[3],n[5])

		final['COUNTY'] = n[4]
		final['AREANAME'] = n[6]
		final['POP'] = newPop
		newPop = 0
		finalOutput.append(final)
	return finalOutput


if __name__ == '__main__':


	popFiles = ["1900Pop.csv",[9,10],"1910Pop.csv",[9,10],"1920Pop.csv",[11,12],"1930Pop.csv",[9],"1940Pop.csv",[9],"1950Pop.csv",[9,13],"1960Pop.csv",[8,15],"1970Pop.csv",[15]]
	outputName = "allPopData.csv"

	allYearOutputs = {'1900': 'fill','1910': 'fill','1920': 'fill','1930': 'fill','1940': 'fill','1950': 'fill','1960': 'fill','1970': 'fill'}

	for i in range(len(popFiles)/2):
		## read all 

		readInfo = readPopulationData(popFiles[i*2])
		arrayOfIndex =popFiles[(i*2)+1]
		final = process(readInfo, arrayOfIndex)

		if i == 0:
			allYearOutputs['1900'] = final
		elif i == 1:
			allYearOutputs['1910'] = final
		elif i == 2:
			allYearOutputs['1920'] = final
		elif i == 3:
			allYearOutputs['1930'] = final
		elif i == 4:
			allYearOutputs['1940'] = final
		elif i == 5:
			allYearOutputs['1950'] = final
		elif i == 6:
			allYearOutputs['1960'] = final
		else:
			allYearOutputs['1970'] = final
 
	print allYearOutputs['1900']




	# convertToCSV(outputName,final)
	