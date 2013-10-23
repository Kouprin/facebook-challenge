import csv

f = open("tags_popularity.tsv")

tags = set()

for line in f:
    if (int(line.strip().split('\t')[1]) < 500):
        break
    line = line.strip().split('\t')[0]
    tags.add(line)

true = 0
fp = 0
fn = 0
with open('Test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        break
    x = 0
    for row in reader:
        x += 1
        if (x % 10000000 == 0):
            print x, true, fp, fn
            precision = true * 1.0 / (true + fp)
            recall = true * 1.0 / (true + fn)
            f1 = 2.0 * precision * recall / (precision + recall)
            print "precision = ", precision
            print "recall = ", recall
            print "f1 = ", f1
        tags_here = []#row[3].strip().split(' ')
        prev = "AAAAAAAAAAAAAAAAAAAAAAAAA"
        already = set()
        for word in row[1].strip().split(' '):
            word = word.lower()
            if (word in already):
                continue
            if (word in tags):
                already.add(word)
                if (word in tags_here):
                    true += 1
                else:
                    #print row
                    fp += 1
            if (prev + "-" + word in tags):
                already.add(word)
                if (prev + "-" + word in tags_here):
                    true += 1
                else:
                    fp += 1
            prev = word
        for tag in tags_here:
            if (tag in already):
                pass
            else:
                fn += 1
        ans = row[0] + "\t"
        for tag in already:
            ans = ans + tag + " "
        print ans

print true, fp, fn
precision = true * 1.0 / (true + fp)
recall = true * 1.0 / (true + fn)
f1 = 2.0 * precision * recall / (precision + recall)
print "precision = ", precision
print "recall = ", recall
print "f1 = ", f1
