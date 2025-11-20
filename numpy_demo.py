from numpy import *

# array()
print("# array()")
arr = array([3, 1, 2])
# add 5 in each value
print(arr + 5)

arr1 = array([1, 2, 3], int)

# vectorized Operations
print(arr + arr1)

# sum of array
print(sum(arr))

print(sort(arr))

print(concatenate([arr, arr1]))

# copy, view, shallow copy, deep copy
