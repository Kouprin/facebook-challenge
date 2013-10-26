import csv
import sys
import os

if (len(sys.argv) != 2):
    print "Run: python test_answer.py <testset>"
    sys.exit(0)

testset = sys.argv[1]


linenum = 0

d = {}
for i in xrange(6034196, 12047532 + 1):
    d[i] = ""

pred = os.listdir("./predictions")
print >> sys.stderr, len(pred), pred
for fil in pred:
    g = open("./predictions/" + fil)
    for line in g:
        line = line.strip()
        d[int(line)] = d[int(line)] + " " + fil[:-5]

x = 6034196
f = open(testset)

tp = 0
fp = 0
fn = 0

for row in f:
    row = row.strip().split('\t')[-1]
    correct_tags = row.strip().split(' ')
    tags = d[x].strip().split(' ')
    #if (correct_tags != ['']):
    #    print tags, correct_tags

    for tag in tags:
        if (tag == ''):
            continue
        if (tag in correct_tags):    
            tp = tp + 1
        else:
            fp = fp + 1

    for tag in correct_tags:
        if (tag == ''):
            continue
        if (tag in tags):
            pass
        else:
            fn = fn + 1

    x += 1

p = tp * 1.0 / (tp + fp + 1e-15)
r = tp * 1.0 / (tp + fn + 1e-15)
f1 = 2.0 * p * r / (p + r + 1e-15)
#print >> sys.stderr, tp, fn, fp
fi = open("./tmp/score", "a")
fi.write(str(tp) + "\t" + str(fp) + "\t" + str(fn) + "\t" + str(p) + "\t" + str(r) + "\t" + str(f1) + "\n")
print >> sys.stderr, p,r,f1
