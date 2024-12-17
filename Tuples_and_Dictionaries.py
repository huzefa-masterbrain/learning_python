d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k , v)

    tups = d.items()
    print(tups)

#     the items() method in dictionaries returns a list of (key , value) tuples

# Tuples are comparable
# The comparison operators work with tuples and other sequence
# If the first item is equal , python goes on to the next element,and so on,until it finds element that differ.

# (0,1,2) < (5,1,2)
#True:output

# (0,1,2000000) < (0,3,4)
# True:output

# ('jones' , 'sally') < ('jones' , 'sam')
# output:True