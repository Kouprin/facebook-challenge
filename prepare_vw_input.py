import csv
import sys

if (len(sys.argv) != 4):
    print "Run: python prepare_vw_input.py <tag> <input_filename> <output_filename>"
    sys.exit(0)

glotag = sys.argv[1]
filename = sys.argv[2]
outp = sys.argv[3]

f = open(filename)
g = open(outp, "w")

for row in f:
    row = row.strip().split("\t")
    if (len(row) < 4):
        el = []
    else:
        el = row[3].strip().split(" ")
    fnd = False
    for word in el:
        if (word.lower() == glotag):
            fnd = True

    outline = "+1 |"
    if (fnd == False):
        outline = "-1 |"

    el = row[1].strip().split(" ")
    for word in el:
        if (word == ""):
            print >> sys.stderr, "hell"
            continue
        outline = outline + " " + word# + "__L"

    #for i in xrange(len(el) - 1):
    #    if (el[i + 1] != 'code__C'):
    #        outline = outline + " " + el[i] + "_" + el[i + 1]

    #for i in xrange(len(el) - 2):
    #    if (el[i + 2] != 'code__C'):
    #        outline = outline + " " + el[i] + "_" + el[i + 1] + "_" + el[i + 2]

    #el = row[2].strip().split(" ")
    #for word in el:
    #    if (word == ""):
    #        continue
    #    outline = outline + " " + word

    g.write(outline + "\n")
