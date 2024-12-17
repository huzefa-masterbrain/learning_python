
# Even though dictionaries are not stored in order we can write a for loop that goes throught all
# the entries in a dictionary actually it goes through all of the keys in the dictionary and looks up the value

counts = {'chuck':1 , 'fred':42 , 'jan':100 }
for key in counts:
    print(key , counts[key])

# Retrieving lists of keys and values
# you can get a list of keys , values , or items (both) for a dictionary

jjj = {'chuck' : 1 , 'fred' : 42 , 'jan' : 100}
print(list(jjj))

print(jjj.keys())
print(jjj.values())
print(jjj.items())