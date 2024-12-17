a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
print(a)
# list can be sliced using:
t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
#  builiding a list from scratch
#  we can create an empty list and then add element using the append method
# the list stay in order and new elements are added at the of the list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
# is something in a list ?
# pyhon provide two operators that return true of false
# they do not modify the list
some = [1,9,21,10,16]
9 in some
15 in some
20 not in some
# lists are in order
# a list can hold many items and keep these items in the order until we do something to change the order
# a list can be sorted (ie.change its order)
# the sort method (unlike in string)means "sort yourself"
friends = ['joseph','glenn','sally']
friends.sort()
print(friends)
print(friends[1])
# built in functions and list
# there are number of functions built into python that takes list as parameters
# remember the loops we built ? these are much simpler
num = [3,41,12,9,74,15]
print(len(num))
print(max(num))
print(min(num))
print(sum(num))
print(sum(num)/len(num))
