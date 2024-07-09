
def binary_search(array, value, min_i, max_i):
    # End search if min exceeds max
    if min_i >= max_i:
        # Return the index of the value if exists, else return the index to add new value
        return min_i - 1 if array[min_i - 1] == value else min_i
    else:
        # Get the midpoint
        mid = min_i + (max_i - min_i) // 2
        # Perform the binary search
        if array[mid] > value:
            return binary_search(array, value, min_i, mid)
        else:
            return binary_search(array, value, mid + 1, max_i)

# Test for binary search
list1 = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
ind = binary_search(list1, 55, 0, len(list1))
print("The target is at {}, and the target is {}".format(ind, list1[ind]))
ind = binary_search(list1, 4, 0, len(list1))
print("The target is at {}, and the target is {}".format(ind, list1[ind]))