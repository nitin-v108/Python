from numpy import *

"""
array()
linspace()
longspace()
arange()
zeros()
ones()
"""

# array()
print("# array()")
arr = array([1, 2, 3])
print(arr)
arr1 = array([1, 2, 3], int)
print(arr1.dtype)
arr2 = array([1, 2, 3, 4.0])
print(arr2.dtype)

# linspace(start,stop,step)
print("\n# linspace(start,stop,step)")
lins1 = linspace(0, 15, 16)
print(lins1)

# logspace(start,end,space)
als1 = logspace(1, 10, 5)
print("\n# #logspace(start,end,space)")
print(als1)


# arange(start,end,steps)
print("\n# arange(start,end,steps)")
arn1 = arange(1, 15, 2)
print(arn1)

# zeros
z1 = zeros(5)
print(z1)


# ones

o1 = ones(5)
print(o1)
