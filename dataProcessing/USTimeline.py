import csv 
allInformation = []

with open('usTimeline.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		allInformation.append(row)


newFormation =[]

for i in range(0, len(allInformation)):
	if i+1 < len(allInformation)-2:
		if len(allInformation[i+1])<4:
			allInformation[i].append(allInformation[i+1])
			newFormation.append(allInformation[i])

	thisPotYear = allInformation[i][0]
	print(thisPotYear.isdigit())
	print thisPotYear
	print type(thisPotYear)
	if thisPotYear.isdigit():
		newFormation.append(allInformation[i])
	if allInformation[i][0]=='':
		year = newFormation[len(newFormation)-1][0]
		allInformation[i][0] = year
		newFormation.append(allInformation[i])

for n in newFormation:	
	print n

