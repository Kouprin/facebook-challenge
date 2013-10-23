import csv
import re

split_rule = '\'|\"|:|;|\. |,| |\*|\n|\t|\(|\)|\?|\!|\\|/|\{|\}|\<|\>|[|]'

f = open("current_tag.tmp")
glotag = f.read().strip()

g = open("vw_output.tmp")


with open('Train.csv', 'rb') as f:
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
            if (score > -2.0):
                tp += 1
            else:
                fn += 1
        elif (score > -2.0):
            fp += 1

        linenum += 1
        if (linenum % 100000 == 0):
            p = tp * 1.0 / (tp + fp)
            r = tp * 1.0 / (tp + fn)
            f1 = 2.0 * p * r / (p + r)
            print "precision = ", p
            print "recall = ", r
            print "f1 = ", f1


        #el = row[2].strip()
        #el = re.split(split_rule, el)
        #for word in el:
        #    if (word == ""):
        #        continue
        #    outline = outline + " " + word.lower()

