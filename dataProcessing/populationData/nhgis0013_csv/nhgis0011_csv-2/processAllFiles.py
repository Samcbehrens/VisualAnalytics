import datetime
import calendar
import json
import csv
import pprint

def convertToCSV(outputFileName, contents):
	
	f = open(outputFileName, 'wt')
	try:
		writer = csv.writer(f)
		writer.writerow( ( 'id', 'state','county', 'areaname', 'pop1900', 'pop1910','pop1920','pop1930','pop1940', 'pop1950','pop1960','pop1970') )

		for keys,values in contents.items():
			writer.writerow((keys, values['STATE'], values['COUNTY'], values['AREANAME'], values['POP'], values['POP10'],values['POP20'],values['POP30'],values['POP40'],values['POP50'],values['POP60'],values['POP70']))
	except csv.Error, e:
		print "problem"
		print (e)
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

	# pp = pprint.PrettyPrinter(indent=4)
	# pp.pprint(formatFile)

def readPopulationData(fileName):
	allInformation = []
	
	with open(fileName, 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
		csvfile.seek(0)
		reader=csv.reader(csvfile,dialect)
		for line in reader:
			allInformation.append(line)
	return allInformation

def checkIfExists(findId, dateDictionary):
	if findId in dateDictionary:
		return True
	else:
		return False


def compileAllDates(DateDictionary):
	allCounties = {}
	
	template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	
	date ='1900'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		keyExists = checkIfExists(checkId, allCounties)
		if  keyExists == False:
			## assign population at that date 
			template['POP'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP'] = DateDictionary[date][i]['POP']

	date ='1910'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		# print checkId
		keyExists = checkIfExists(checkId, allCounties)
		# print keyExists
		if  keyExists == False:
			## assign population at that date 
			template['POP10'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP10'] = DateDictionary[date][i]['POP']


	date ='1920'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		# print checkId
		keyExists = checkIfExists(checkId, allCounties)
		# print keyExists
		if  keyExists == False:
			## assign population at that date 
			template['POP20'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP20'] = DateDictionary[date][i]['POP']

	date ='1930'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		# print checkId
		keyExists = checkIfExists(checkId, allCounties)
		# print keyExists
		if  keyExists == False:
			## assign population at that date 
			template['POP30'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP30'] = DateDictionary[date][i]['POP']

	date ='1940'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		# print checkId
		keyExists = checkIfExists(checkId, allCounties)
		# print keyExists
		if  keyExists == False:
			## assign population at that date 
			template['POP40'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP40'] = DateDictionary[date][i]['POP']


	date ='1950'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		# print checkId
		keyExists = checkIfExists(checkId, allCounties)
		# print keyExists
		if  keyExists == False:
			## assign population at that date 
			template['POP50'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP50'] = DateDictionary[date][i]['POP']


	date ='1960'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		# print checkId
		keyExists = checkIfExists(checkId, allCounties)
		# print keyExists
		if  keyExists == False:
			## assign population at that date 
			template['POP60'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP60'] = DateDictionary[date][i]['POP']


	date ='1970'
	for i in range(len(DateDictionary[date])):
		checkId = DateDictionary[date][i]['ID']
		# print checkId
		keyExists = checkIfExists(checkId, allCounties)
		# print keyExists
		if  keyExists == False:
			## assign population at that date 
			template['POP70'] = DateDictionary[date][i]['POP']
			template['STATE'] = DateDictionary[date][i]['STATE']
			template['COUNTY'] = DateDictionary[date][i]['COUNTY']
			template['AREANAME'] = DateDictionary[date][i]['AREANAME']
			#add to all county key container 
			allCounties[checkId] = template
			#reset 
			template= {'STATE': 'fill','COUNTY': 'fill','AREANAME': 'fill','POP':'fill','POP10': 'fill','POP20': 'fill','POP30': 'fill','POP40': 'fill','POP50': 'fill','POP60': 'fill','POP70': 'fill'}
	 	else:
			#key exists so just assign that years pop to key 
			allCounties[checkId]['POP70'] = DateDictionary[date][i]['POP']

	return allCounties

## census changed format in 1970s. This is a way of compensating
def specialProcess(allInformation, ArrayOfIndex):
	finalOutput = []
	for n in allInformation:
		addEvent={'YEAR': 'fill', 'STATE': 'fill', "ID" : "fill" ,'COUNTY': 'fill','AREANAME': 'fill','POP': 'fill'}
		testPop = n[ArrayOfIndex[0]]

		if testPop.isdigit(): 
			newPop = int(testPop)
		else:
			newPop = 0

		final = addEvent
		final['YEAR'] = n[1]
		final['STATE'] = n[2]

		countyId = n[3]+n[5]
		countyId = countyId.lstrip('0')

		final['ID'] = countyId
		final['COUNTY'] = n[4]
		final['AREANAME'] = n[14]
		final['POP'] = newPop
		newPop = 0
		finalOutput.append(final)
	return finalOutput
			
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
			testPop = n[ArrayOfIndex[0]]
			if testPop.isdigit(): 
				newPop = int(testPop)
			else:
				newPop = 0

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
			final = specialProcess(readInfo, arrayOfIndex)
			allYearOutputs['1970'] = final

 
	allCounties = compileAllDates(allYearOutputs)

	# for keys,values in allCounties.items():
	# 	print(keys)
	# 	print(values)
    
	convertToCSV(outputName,allCounties)
	