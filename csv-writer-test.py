import csv

data = []

item = ['foo', 5, 18]
data.append(item)

item = ['bar', 11, 234]
data.append(item)

item = ['Robert', 59, 4]
data.append(item)

print(data)

with open('./test-data.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerows(data)
	
csvFile.close()

