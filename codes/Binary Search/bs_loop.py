
def binary_search(array, value):
    # Get the min, max of the search space (in this case is the index)
    left, right = 0, len(array)
    # Loop through the array
    while left < right:
        # Get the midpoint
        mid = left + (right - left) // 2
        # Perform binary search
        if array[mid] > value:
            right = mid
        else:
            left = mid + 1
    
    # Return the index of the location where the value is
    if array[left - 1] == value:
        return left - 1
    # Return the index where the value needs to go in
    else:
        return left

# Test for binary search
list1 = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
ind = binary_search(list1, 13)
print("The target is at {}, and the target is {}".format(ind, list1[ind]))
ind = binary_search(list1, 100)
print("The target is at {}, and the target is {}".format(ind, list1[ind]))

