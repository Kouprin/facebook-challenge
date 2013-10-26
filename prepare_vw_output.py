import sys

if (len(sys.argv) != 4):
    print "Run: python prepare_vw_output.py <border> <input_vw> <output_pred>"
    sys.exit(0)

border = float(sys.argv[1])
f = open(sys.argv[2])
g = open(sys.argv[3], "w")

x = 0
for line in f:
    d = float(line.strip())
    if (d > border):
        g.write(str(x + 6034196) + "\n")
    x += 1
