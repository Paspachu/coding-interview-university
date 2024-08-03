import random

def sort(arr, left, right):
    if left == right:
        return
    
    i = left
    j = right
    pivot_ind = random.randint(left, right)
    pivot_val = arr[pivot_ind]

    while i < j:
        while arr[i] < pivot_val:
            i += 1
        while arr[j] > pivot_val:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if left < j:
        sort(arr, left, j)
    if right > i:
        sort(arr, i, right)

def quicksort(arr):
    sort(arr, 0, len(arr)-1)

# Initialize array for test
arr = [3, 1, 4, -1, 5, 9, 2, 6, -5, -3, -5, -9]
print(arr)
quicksort(arr)
print(arr)