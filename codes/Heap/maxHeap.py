
class MaxHeap:
    # This heap is for zero indexed array.
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.H = [None] * self.maxSize

    def print_heap(self):
        print(self.H[:self.size])

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2

    def sift_up(self, i):
        # Loop until the root
        while i > 0:
            p = self.parent(i)
            # If the parent is greater than or equal to the new value, then stop sifting up
            if self.H[p] >= self.H[i]:
                break
            self.H[p], self.H[i] = self.H[i], self.H[p]
            i = p

    def insert(self, val):
        # If the heap is full, raise an error
        if self.size >= self.maxSize:
            raise Exception("The heap is full.")
        # Insert new value to the heap and siftup
        self.H[self.size] = val
        self.sift_up(self.size)
        self.size += 1

    def get_max(self):
        return self.H[0]
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def sift_down(self, i):
        max_index = i
        # Compare the current value with its left child
        l = self.left_child(i)
        if l < self.size and self.H[l] > self.H[max_index]:
            max_index = l
        # Compare the current value with its right child
        r = self.right_child(i)
        if r < self.size and self.H[r] > self.H[max_index]:
            max_index = r
        # Sift down if necessary
        if i != max_index:
            self.H[i], self.H[max_index] = self.H[max_index], self.H[i]
            self.sift_down(max_index)

    def extract_max(self):
        # Get the output to return
        output = self.H[0]
        # Move the rightmost value in the heap to root
        self.H[0], self.H[self.size - 1] = self.H[self.size - 1], None
        # Decrease the size of the heap and sift down the moved value
        self.size -= 1
        self.sift_down(0)
        return output

    def remove(self, i):
        # Change the value of ith element in the heap to infinity
        self.H[i] = float('inf')
        # Sift up the ith value and extract max
        self.sift_up(i)
        self.extract_max()

# Simply inserting takes O(n log n) time while this method takes O(n) time
def heapify(arr):
    n = len(arr)
    # Initialize a new heap
    new_heap = MaxHeap(n)
    # Copy given array to new heap
    new_heap.size = n
    new_heap.H = arr
    # Sift down all indices from the second highest level
    for i in range(n // 2 - 1, -1, -1):
        new_heap.sift_down(i)
    return new_heap

# TODO: The logic is good but can be improved based on the use cases
def heap_sort(heap):
    size = heap.size
    n = heap.size - 1
    for _ in range(n):
        heap.H[0], heap.H[n] = heap.H[n], heap.H[0]
        heap.size = n
        n -= 1
        heap.sift_down(0)
    heap.size = size



def main():
    # Initialization for testing
    h1 = MaxHeap(15)
    h1.print_heap()

    # Test for insert and siftup
    h1.insert(5)
    h1.insert(3)
    h1.insert(17)
    h1.insert(10)
    h1.insert(84)
    h1.insert(19)
    h1.insert(6)
    h1.insert(22)
    h1.insert(9)
    h1.insert(7)
    h1.insert(33)
    h1.insert(11)
    h1.print_heap()

    # Test for get_max
    print("The max value in the heap is {}.".format(h1.get_max()))

    # Test for get_size
    print("The size of the heap is {}.".format(h1.get_size()))

    # Test for is_empty
    h1.print_heap()
    print(h1.is_empty())
    h2 = MaxHeap(10)
    print(h2.is_empty())

    # Test for extract_max
    print("The max value in the heap is {}.".format(h1.extract_max()))
    h1.print_heap()
    print("The size of the heap is {}.".format(h1.get_size()))
    print("The max value in the heap is {}.".format(h1.extract_max()))
    h1.print_heap()
    print("The size of the heap is {}.".format(h1.get_size()))

    # Test for remove
    h1.remove(4)
    h1.print_heap()

    # Test for heapify
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    h2 = heapify(arr1)
    h2.print_heap()

    # Test for heap_sort
    heap_sort(h2)
    h2.print_heap()
    heap_sort(h1)
    h1.print_heap()

if __name__ == '__main__':
    main()



