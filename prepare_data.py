import csv
import sys
import re

split_rule = '/\\:;,*?!&()[]<>{}=\t\n\'"`$|'

def mysplit(string):
    here = []
    for char in string:
        if (char in split_rule) or (ord(char) > 127) or (ord(char) < 32):
            here.append(" ")
        else:
            here.append(char)
    return "".join(here)

f = open("./data/trash_words.tsv")

kill = set()

for line in f:
    line = line.strip().split("\t")
    kill.add(line[0])

records = []

ff = open("./data/test.tsv", "w")

x = 0
with open("./data/Test.csv", "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        break
    for row in reader:
        x += 1
        wrt = []
        current = [str(len(row[1] + row[2]))]
        for rec in row[1:]:
            rec = mysplit(rec)
            rec = rec.split(" ")
            here = []
            for z in rec:
                if (z == ""):
                    continue
                if (z[-1] == '.'):
                    z = z[:-1]
                if (z.lower() in kill):
                    continue
                if (z.upper() == z) and (z.lower() != z):
                    z = z.lower() + "__U"
                else:
                    z = z.lower()
                if (z != ""):
                    here.append(z)

            current.append(" ".join(here))
        if ("<code>" in row[2]):
            current[1] = current[1] + " code__C"

        #records.append("\t".join(current))

        if (x % 10000 == 0):
            print >> sys.stderr, x
        ff.write("\t".join(current) + "\n")

#records.sort()

#prev = ""
#for line in records:
#    if (prev != line):
#        if (prev != ""):
#            #print prev
#    prev = line

#print prev
