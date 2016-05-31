import csv

file1 = open("file1.csv", "r")
file2 = open("file2.csv", "r")

csv_reader1 = csv.reader(file1)
next(csv_reader1, None)
csv_reader2 = csv.reader(file2)
next(csv_reader2, None)

dict1 = {}
for row in csv_reader1:
    dict1[row[0],row[1]] = row[2]
dict2 = {}
for row in csv_reader2:
    dict2[row[0],row[1]] = row[3]

for key, value in dict1.iteritems():
    print key, value

for key, value in dict2.iteritems():
    print key, value

for key, value in dict1.iteritems():
    if key in dict2.keys():
        #print int(value) - int(dict2[key])
        print( int(value) - int(dict2[key]) )
