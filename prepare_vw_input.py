import csv
import sys
import re

split_rule = '\'|\"|:|;|\. |,| |\*|\n|\t|\(|\)|\?|\!|\\|/|\{|\}|\<|\>|[|]'

if (len(sys.argv) != 4):
    print "Run: python prepare_vw_input.py <tag> <input_filename> <output_filename>"
    sys.exit(0)

glotag = sys.argv[1]
filename = sys.argv[2]
outp = sys.argv[3]

g = open(outp, "w")

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        break
    for row in reader:
        if (len(row) < 4):
            el = ""
        else:
            el = row[3].strip()
        el = re.split(split_rule, el)
        fnd = False
        for word in el:
            if (word.lower() == glotag):
                fnd = True

        outline = "+1 |"
        if (fnd == False):
            outline = "-1 |"

        el = row[1].strip()
        el = re.split(split_rule, el)
        for word in el:
            if (word == ""):
                continue
            outline = outline + " " + word.lower()# + "?L"
            if (word.upper() == word):
                outline = outline + "___U"

        #el = row[2].strip()
        #el = re.split(split_rule, el)
        #for word in el:
        #    if (word == ""):
        #        continue
        #    outline = outline + " " + word.lower()

        g.write(outline + "\n")
