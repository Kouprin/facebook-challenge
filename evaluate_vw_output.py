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
f = open(filename)

tp = {}
fp = {}
fn = {}
for x in xrange(200):
    tp[x] = 0
    fp[x] = 0
    fn[x] = 0

linenum = 0

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

    for x in xrange(200):
        border = -x / 10.0
        if (fnd):
            if (score > border):
                tp[x] = tp[x] + 1
            else:
                fn[x] = fn[x] + 1
        elif (score > border):
            fp[x] = fp[x] + 1

    linenum += 1
    if (linenum % 50000 == 0):
        break

maxf1 = -1.0
border = 0.0
for x in xrange(200):
    p = tp[x] * 1.0 / (tp[x] + fp[x] + 1e-15)
    r = tp[x] * 1.0 / (tp[x] + fn[x] + 1e-15)
    f1 = 2.0 * p * r / (p + r + 1e-15)
    #print >> sys.stderr, p,r,f1
    if (p > 0.25) and (f1 > maxf1):
        maxf1 = f1
        border = -x / 10.0
        #print >> sys.stderr, border, p,r,f1

print >> sys.stderr, "border =", border, " f1 =", maxf1
print border
