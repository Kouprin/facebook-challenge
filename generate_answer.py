import os
import sys

f = open("./tmp/tmp", "w")

d = {}
for i in xrange(6034196, 8047532 + 1):
    d[i] = ""

pred = os.listdir("./predictions")
print pred
for fil in pred:
    g = open("./predictions/" + fil)
    for line in g:
        line = line.strip()
        d[int(line)] = d[int(line)] + " " + fil[:-5]

g = open("./data/correctly_predicted.tsv")
for line in g:
    line = line.strip().split('\t')
    d[int(line[0])] = line[1]

#g = open("./data/badly_predicted.tsv")
#for line in g:
#    line = line.strip().split('\t')
#    if (d[int(line[0])] == "") and (len(line) > 1):
#        d[int(line[0])] = line[1]

f.write('"Id","Tags"' + '\n')
for i in xrange(6034196, 8047532 + 1):
    #if (d[i].strip() == ""):
        #d[i] = "c# java php javascript android"
    f.write(str(i) + ',"' + d[i].strip() + '"\n')
