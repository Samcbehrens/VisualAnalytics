import csv 
allInformation = []

with open('usTimeline.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		allInformation.append(row)

print allInformation