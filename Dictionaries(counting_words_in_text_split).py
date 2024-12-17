counts = dict()
print('enter a line of text:')
line = input('')
words = line.split()
print('words:', words)
print('counting ....')
for word in words:
    counts[word] = counts.get(word, 0) + 1
    print('counts', counts)

    # the general pattern to count the words in a line of text is to split the line into words , then loop through the
    # words and use a dictionary to track the count of each word independently.

counts = dict()
line = input('Enter a line of text:')
words = line.split()
print('words:' , words)
print('counting...')

for word in words:
    counts[word] = counts.get(word , 0) + 1
    print('counts' , counts)