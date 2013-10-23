import csv
import re

split_rule = '\'|\"|:|;|\. |,| |\*|\n|\t|\(|\)|\?|\!|\\|/|\{|\}|\<|\>|[|]'

f = open("./data/trash_words.tsv")

kill = set()

for line in f:
    line = line.strip().split("\t")
    kill.add(line[0])

records = []

with open("./data/Train.csv", "rb") as f:
    reader = csv.reader(f)
    for row in reader:
        break
    for row in reader:
        wrt = []
        for rec in row[1:]:
            rec = re.split("<code>|</code>", rec)
            rec = re.split(split_rule, rec)
            wrt.append(rec)


        records.append("\t".join(wrt))

records.sort()

prev = ""
for line in records:
    if (prev != line):
        print prev
    prev = line

print prev
