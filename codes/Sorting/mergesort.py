
def merge(arr, low, mid, high):
    m = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            m.append(arr[i])
            i += 1
        else:
            m.append(arr[j])
            j += 1

    while i <= mid:
        m.append(arr[i])
        i += 1

    while j <= high:
        m.append(arr[j])
        j += 1

    for ind, val in enumerate(m):
        arr[low+ind] = val

def sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        sort(arr, low, mid)
        sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def mergesort(arr):
    sort(arr, 0, len(arr)-1)

# Initialize array for test
arr = [3, 1, 4, -1, 5, 9, 2, 6, -5, -3, -5, -9]
print(arr)
mergesort(arr)
print(arr)