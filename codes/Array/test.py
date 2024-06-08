import numpy as np

# Create an array with natural numbers up to 10
arr = np.arange(1, 11)
print(arr)

# Get the size of array, generally there is no capacity limit
print(arr.size)

# Test if the array is empty
print(arr.size == 0)

# You can create empty array using empty in numpy
print(np.empty([1, 10]))

# Accessing element in array
print(arr[4]) # should get 5, since index starts at 0
# print(arr[27]) # should print out IndexError

# Add new element to array
print(arr.append(11))





