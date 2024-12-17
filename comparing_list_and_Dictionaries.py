
# dictionaries are like lists except that they use key instead of number to look up values.

lst = list()
lst.append(21)
lst.append(183)
print(lst)

lst[0] = 23
print(lst)

add = dict()
add['age'] = 21
add['course'] = 182
print(add)

add['age'] = 23
print(add)

# you can make an empty dictionary using empty curly braces

jjj = {'Chuck':1,'fred':42,'jan':100}
print(jjj)

ooo = {}
print(ooo)

# MOST COMMON NAME?
# One common use of dictionaries is counting how often we "see" something

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)


