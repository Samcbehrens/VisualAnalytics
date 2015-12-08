import csv 

def readCsv():

	allInformation = []

	with open('usTimeline.csv', 'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
		csvfile.seek(0)
		reader=csv.reader(csvfile,dialect)
		for line in reader:
			allInformation.append(line)
	return allInformation

def reformat(allInformation):

	newFormation =[]

	for i in range(0, len(allInformation)):

		
		## get index out of range if you dont check this first
		if i+1 < len(allInformation)-1:
			##look ahead to see if the next one doesnt have a date
			if allInformation[i+1][0]=='':
				allInformation[i+1][0]=allInformation[i][0]

		#add if it has the correct date
		thisPotYear = allInformation[i][0]
		if thisPotYear.isdigit():
			newFormation.append(allInformation[i])

	return newFormation


if __name__ == '__main__':
	allInformation = readCsv()
	newFormation = reformat(allInformation)

	for n in newFormation:	
		print n

