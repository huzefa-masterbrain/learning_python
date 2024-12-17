# best friends:strings and lists
abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
print(stuff)
for w in stuff:
    print(w)
#split breaks a string into parts and produces a list of strings
# we think of these as words.we can access a particular word or loop through all the words
line = 'a lot    of space'
etc = line.split()
print(etc)

line = 'frist;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))
# when you do not specify a delimiter,multiple spaces are treated like one delimiter
# you can specify what delimiter character to use in the splitting

