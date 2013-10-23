import csv
import sys

m = dict()

with open('Train.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        break
    for row in reader:
        m[row[1] + "\n" + row[2]] = row[3]
        #print row

with open('Test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        break
    for row in reader:
        if (m.has_key(row[1] + "\n" + row[2])):
            print row[0] + "\t" + m[row[1] + "\n" + row[2]]
            #print >> sys.stderr, row[0] + "\t" + m[row[1] + row[2]]
        #print row
