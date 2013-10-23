import sys
d = {}

f = open("./data/train.tsv")
ln = 0
for line in f:
    if (ln % 100000 == 0):
        print >> sys.stderr, ln
    ln += 1
    line = " ".join(line.split("\t")).split(" ")
    for z in line:
        if (d.has_key(z)):
            d[z] += 1
        else:
            d[z] = 1

print >> sys.stderr, "OK"

a = []
for z in d:
    a.append((d[z], z))

print >> sys.stderr, "OK"
a.sort(reverse=True)
print >> sys.stderr, "sorted"

for z in a:
    print z[1] + "\t" + str(z[0])
