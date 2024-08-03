
def bubblesort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Initialize array for test
arr = [3, 1, 4, -1, 5, 9, 2, 6, -5, -3, -5, -9]
print(arr)
bubblesort(arr)
print(arr)