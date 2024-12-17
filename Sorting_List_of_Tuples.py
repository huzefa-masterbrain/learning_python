
# we can take advantage of the ability to sort a list of tuples to get a sorted version of a dictionaries
# Frist we sort the dictionary by the key using the items() method and the sorted() function

d = {'a' : 10 , 'b' : 1 , 'c' : 22}
print(d.items())
print(sorted(d.items()))

# using sorted()
# we can do this even more directly using the build-in-function sorted that takes a sequence as a parameter and
# return a sorted sequences

d = {'a':10,'b':1,'c':22}
t = sorted (d.items())
print(t)
for k , v in sorted(d.items()):
    print(k , v)

    # sort by values instead of key
    # if we could construct a list of tuples of the from (value , key) we could sort by value
    # we do this with a for loop that creates a list of tuples

    c = {'a':10 , 'b':1 , 'c':22}
    tmp = list()
    for k,v in c.items():
        tmp.append((v,k))
        print(tmp)

        tmp = sorted(tmp , reverse=True)
        print(tmp)

        # NB: by applying reverse = True if sort by decending order value and key.
