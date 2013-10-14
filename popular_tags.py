import sys

f = open("train.tsv")

d = {}

for line in f:
    tags = line.strip().split('\t')[-1].split(' ')
    for tag in tags:
        if (tag == "+"):
            print line
            sys.exit()
        if (d.has_key(tag) == False):
            d[tag] = 1
        else:
            d[tag] += 1

inp = []
sum = 0
for tag in d:
    inp.append((d[tag], tag))
    sum += d[tag]

inp.sort(reverse=True)

cur = 0
for tag in inp:
    cur += tag[0]
    print tag[1] + "\t" + str(tag[0]) + "\t" + str(tag[0] * 1.0 / sum) + "\t" + str(cur * 1.0 / sum)
