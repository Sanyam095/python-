# MAP
# ye ek higher order function hai mtlb ye ek function ko as an argument leta hai
def cube(x):
    return x**3 

print(cube(2))

l = [1,2,4,6,4,3]

# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube, l))
print(newl)

#FILTER
# ye ek higher order function hai mtlb ye bhi ek function ko as an argument leta hai
def filter_function(a):
    return a>2

newnewl = list(filter(filter_function, l))
print(newnewl)


# REDUCE
# phli bat to ye ki reduce ko use krne se phle use import krna hota hai

from functools import reduce
sum = reduce(lambda x,y: x+y, l)

print(sum)