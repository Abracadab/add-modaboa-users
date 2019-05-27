import csv

filename = './test-data.csv'
delim = ','

data = []

item = ['foo', 5, 18]
data.append(item)

item = ['bar', 11, 234]
data.append(item)

item = ['Robert', 59, 4]
data.append(item)

item = ['Josephine', 59, 4]
data.append(item)

print(data)

with open(filename, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile, delimiter=delim)
    writer.writerows(data)

csvFile.close()

