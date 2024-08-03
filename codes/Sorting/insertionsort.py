
def insertionsort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

# Initialize array for test
arr = [3, 1, 4, -1, 5, 9, 2, 6, -5, -3, -5, -9]
print(arr)
insertionsort(arr)
print(arr)