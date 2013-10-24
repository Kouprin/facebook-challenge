import sys

if (len(sys.argv) != 4):
    print "Run: python prepare_vw_output.py <percent> <input_vw> <output_pred>"
    sys.exit(0)

howmany = float(sys.argv[1])
f = open(sys.argv[2])
g = open(sys.argv[3], "w")

a = []
x = 0
for line in f:
    d = float(line.strip())
    a.append((d, x))
    x += 1

a.sort(reverse=True)

count = int(len(a) * howmany)

for i in xrange(count):
    g.write(str(a[i][1] + 6034196) + "\n")




#for line in a:
#    print str(line[0]) + "\t" + str(line[1] + 6034196)
