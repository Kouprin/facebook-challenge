import csv
import sys
import random

if (len(sys.argv) != 4):
    print "Run: python evaluate_vw_output.py <tag> <inputdata_filename> <vwoutput_filename>"
    sys.exit(0)

glotag = sys.argv[1]
filename = sys.argv[2]
outp = sys.argv[3]

g = open(outp)
f = open(filename)

linenum = 0

scores = []

f1 = 0
tp = 0
fn = 0
fp = 0

for row in f:
    row = row.strip().split('\t')
    score = float(g.readline().strip())
    if (len(row) < 4):
        el = []
    else:
        el = row[3].strip().split(' ')
    fnd = False
    for word in el:
        if (word.lower() == glotag):
            fnd = True
            fn = fn + 1

    scores.append((score + random.random() / 1e5, fnd))

    linenum += 1
    if (linenum % 50000 == 0):
        break

scores.sort(reverse=True)

maxf1 = -1
border = 100
R = 0
P = 0
beta = 2

for x in scores:
    if (x[1] == True):
        tp = tp + 1
        fn = fn - 1
    else:
        fp = fp + 1
    p = tp / (tp + fp + 1e-15)
    r = tp / (tp + fn + 1e-15)
    f1 = (1 + beta) * p * r / (beta * beta * p + r + 1e-15)
    #print >> sys.stderr, p,r,f1
    if (f1 > maxf1):
        maxf1 = f1
        border = x[0]
        P = p
        R = r
        #print >> sys.stderr, border, p,r,f1

print >> sys.stderr, "border =", border, " f1 =", maxf1, " p =", P, " r =", R
print border
