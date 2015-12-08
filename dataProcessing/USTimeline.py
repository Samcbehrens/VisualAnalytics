import csv 
allInformation = []

 with open('usTimeline.csv', 'rb') as csvfile:
	dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=',')
	csvfile.seek(0)
	reader=csv.reader(csvfile,dialect)
	for line in reader:
		allInformation.append(line)

newFormation =[]

for i in range(0, len(allInformation)):
	print allInformation[i]
# 	if i+1 < len(allInformation)-2:
# 		if len(allInformation[i+1])<4:
# 			allInformation[i].append(allInformation[i+1])
# 			newFormation.append(allInformation[i])

# 	thisPotYear = allInformation[i][0]
# 	print(thisPotYear.isdigit())
# 	print thisPotYear
# 	print type(thisPotYear)
# 	if thisPotYear.isdigit():
# 		newFormation.append(allInformation[i])
# 	if allInformation[i][0]=='':
# 		year = newFormation[len(newFormation)-1][0]
# 		allInformation[i][0] = year
# 		newFormation.append(allInformation[i])

# for n in newFormation:	
# 	print n

