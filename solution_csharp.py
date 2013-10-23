train = open("train1.tsv")
test = open("train2.tsv")

def addto(line, words):
    x = line.split(' ')
    for word in x:
        if (word != ""):
            if (words.has_key(word)):
                words[word] += 1
            else:
                words[word] = 1


for line in train:
    inp = line.strip().split('\t')
    for x in inp[0:1]:
