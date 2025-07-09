# MAP

def cube(x):
    return x*x*x


print(cube(2))

l = [1, 2, 3, 4, 5]
newl = []

# for item in l:
#     newl.append(cube(item))
    
# print(newl)

# newl = map(cube, l)
# print(newl)

newl = list(map(cube, l))
print(newl)

# newl = list(map(lambda x : x*x*x, l))
# print(newl)



# FILTER
def filter_func(a):
    return a>2

filter_l = list(filter(filter_func, l))
print(filter_l)

filter_l = list(filter(lambda a : a%2==0, l))
print(filter_l) 


# REDUCE
from functools import reduce      

def mySum(x, y):
    return x+y

reduce_l = reduce(mySum, l)
print(reduce_l)

reduce_l = reduce(lambda x, y : x+y, l)
print(reduce_l)