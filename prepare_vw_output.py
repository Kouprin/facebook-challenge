f = open("vw_output.tmp")

a = []
x = 0
for line in f:
    d = float(line.strip())
    a.append((d, x))
    x += 1

a.sort(reverse=True)
for line in a:
    print line[0]
