
def selectionsort(arr):
    for i in range(len(arr) - 1):
        index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i], arr[index] = arr[index], arr[i]

# Initialize array for test
arr = [3, 1, 4, -1, 5, 9, 2, 6, -5, -3, -5, -9]
print(arr)
selectionsort(arr)
print(arr)