fhand = open('collection and dictionries.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word , 0) + 1

        list =list()
        for key , val in counts.items():
            newtup = (val , key)
            lst.append(newtup)
            lst = sorted(lst , reverse = True)
            for val , key in lst [:10]:
                print(key , val)
                # c = {'a': 10, 'b': 1, 'c': 22}
                print(sorted([(v, k for k, v in c.items())]))

# list comprehension creates a dynamic list.in this case we make a list of reversed tuples and then sort it.
# http://wiki.python.org/moin/howto/sorting

x = di.items()
x = sorted(di.items())
print(x)
 x = sorted(di.items())
 print(x[:5])

 tmp = list()
 for k , v in di.items()
     print(k , v)

     tmp = list()
     for k , v in di.items()
         print(k , v)
         newt = (v , k)
         tmp.append(newt)
         print('flipped' , tmp)
         tmp = sorted(tmp)
         print('sorted' , tmp)