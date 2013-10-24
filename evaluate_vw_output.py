import csv
import sys
import re

split_rule = '\'|\"|:|;|\. |,| |\*|\n|\t|\(|\)|\?|\!|\\|/|\{|\}|\<|\>|[|]'

if (len(sys.argv) != 4):
    print "Run: python evaluate_vw_output.py <tag> <inputdata_filename> <vwoutput_filename>"
    sys.exit(0)

glotag = sys.argv[1]
filename = sys.argv[2]
outp = sys.argv[3]

g = open(outp)

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        break
    linenum = 0
    tp = 0
    fp = 0
    fn = 0
    for row in reader:
        score = float(g.readline().strip())
        el = row[3].strip().split(' ')
        fnd = False
        for word in el:
            if (word.lower() == glotag):
                fnd = True

        if (fnd):
            if (score > -10.5):
                tp += 1
            else:
                fn += 1
        elif (score > -10.5):
            fp += 1

        linenum += 1
        if (linenum % 100000 == 0):
            p = tp * 1.0 / (tp + fp + 0.00001)
            r = tp * 1.0 / (tp + fn + 0.00001)
            f1 = 2.0 * p * r / (p + r + 0.00001)
            print "precision = ", p
            print "recall = ", r
            print "f1 = ", f1


        #el = row[2].strip()
        #el = re.split(split_rule, el)
        #for word in el:
        #    if (word == ""):
        #        continue
        #    outline = outline + " " + word.lower()

