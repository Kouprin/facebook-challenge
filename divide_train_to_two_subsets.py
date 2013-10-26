f = open("./data/train.tsv")
a = open("./data/train1.tsv", "w")
b = open("./data/train2.tsv", "w")

x = 2
for line in f:
    if (x == 0):
        a.write(line)
    else:
        b.write(line)

    x = (x + 1) % 4
