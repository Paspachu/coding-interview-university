# Create an array with natural numbers up to 10
arr = [n for n in range(1, 11)]
print(arr)

# Get the size of array, generally there is no capacity limit
print(len(arr))

# Test if the array is empty
print(not arr)
print(not [])

# Accessing element in array
print(arr[4]) # should get 5, since index starts at 0

# Add new element to array at the end
arr.append(11) # append is in-place update
print(arr) 

# Insert element in certain index
arr.insert(3, 31) # insert is in-place update
print(arr)

# Prepend: insert at the front of array
arr.insert(0, 17)
print(arr)

# Pop: remove and return the last element in array
print(arr.pop())
print(arr)
# It is also possible to pop any index
print(arr.pop(4))
print(arr)

# Delete the element at index
del arr[6] # del is in-place update
print(arr)

# Remove the element if it exists in index (if not, ValueError)
arr.remove(9) # remove is in-place update
print(arr)

# Find the index of the first element equal to what we are finding (if there is no such element, raise ValueError)
print(arr.index(8))

# Extend the list
arr.extend([-n for n in range(5)])
print(arr)

# Sort the list
arr.sort()
print(arr)

# Reverse the list
arr.reverse()
print(arr)

# Count how many certain element is in array
print(arr.count(1))

# Clear the list
arr.clear()
print(arr)