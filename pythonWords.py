name = input('enter file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
for words in words:
    counts[words] = counts.get(words, 0) + 1