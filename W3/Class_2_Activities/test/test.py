import csv

with open('test.csv') as testCSV:

    testRead = csv.reader(testCSV)

    for i in testRead:
        print(i)