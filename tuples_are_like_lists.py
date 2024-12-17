
# tuples are another kind of sequence that function much like a list they have elements which are indexed starting at 0

x = ('Glenn' , 'Sally' , 'Joseph')
print(x[2])

y = (1,9,2)
print(y)

for iter in y:
    print(iter)

#     but...Tuples are "IMMUTABLE"
# unlike a list ,once you create a tuple,you cannot alter its contents-similar to a string

x=[9,8,7]
x[2]=6
print(x)

# y='ABC'
# y[2] = 'D'
# TypeError: 'str' object does not support item assignment

# z = (5,4,3)
# z[2] = 0
# TypeError: 'tuple' object does not support item assignment

# things not to do with tuples
# x = (3,2,1)
# x.sort()
# AttributeError: 'tuple' object has no attribute 'sort'

# x = (3,2,1)
# x.append(5)
# AttributeError: 'tuple' object has no attribute 'append'

#  x = (3,2,1)
#  x.__reversed__()
# IndentationError: unexpected indent

# a tale of Two sequences
l= list()
dir(l)

['append' , 'count' , 'extend' , 'index' , 'insert' , 'pop' , 'remove' , 'reverse' , 'sort']
t=tuple()
dir(t)

# Tuples are more efficient
# since python does not have to build tuple structures to be modifiable , they are simpler and more
# efficient in terms of memory use and performance than lists
# so in our program when we are making "temporary variables" we prefer tuples over lists.

# Tuples and Assignment
# we can also put a tuple on the left-hand side of an assignment statement
# we can even omit the parentheses

(x,y) = (4 , 'fred')
print(y)

(a , b) = (99 , 98)
print(a)

