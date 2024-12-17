
# it is an error to reference a key which is not in the dictionary
# we can use the in operator to see if a key is in the dictionary

# ccc = dict()
# print(ccc['csev'])
# output will bring keyERROR : 'csev'

# when we see a new name ,when we encounter A NEW name ,
# we need to add a new entry in the dictionary and if this the second
# or later time we have seen the name ,we simply add one to the count in the dictionary under that name

counts = dict()
names = ['csev' , 'cwen' , 'csev' , 'zqain' , 'cwen']
for names in names:
    if names not in counts:
        counts[names] = 1
    else:
        counts[names] = counts[names] + 1
        print(counts)

# the get method for Dictionaries
# the pattern of checking to see is a key is already in a dictionary and assuming a default value if the key is not
# there is so common that there is a method called get() that does this for us

#  if name in counts:
#     x = counts[name]
# else:
#     x = 0
#     x = counts.get(name,0)
# {'csev' : 2 , 'zqain' : 1 , 'cwen' : 2}
# output:NameError: name 'name' is not defined

# Simplified counting with get()
# we can use get() and provide a default value zero when the key is not yet in the the dictionary and then
# just add one

counts = dict()
names = ['csev' , 'cwen' , 'csev' , 'zqain' , 'cwen']
for name in names:
    counts[name] = counts.get(name ,0) + 1
    print(counts)



