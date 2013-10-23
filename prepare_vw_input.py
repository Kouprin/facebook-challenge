import csv
import re

split_rule = '\'|\"|:|;|\. |,| |\*|\n|\t|\(|\)|\?|\!|\\|/|\{|\}|\<|\>|[|]'

f = open("current_tag.tmp")
glotag = f.read().strip()

g = open("current_vw_data.tmp", "w")

with open('Train.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        break
    for row in reader:
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
