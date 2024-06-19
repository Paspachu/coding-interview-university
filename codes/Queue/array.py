class Queue:
    def __init__(self, size = 10):
        # Assign one more space for buffer
        self.size = size + 1
        self.queue = [None] * self.size        
        self.read = 0
        self.write = 0
    
    def print_queue(self):
        i = self.read
        print_line = ""
        while i != self.write:
            print_line += "{}, ".format(self.queue[i])
            i = (i + 1) % self.size
        print(print_line[:-2])

    def enqueue(self, value):
        # If the queue is full, then raise error
        if self.full():
            raise Exception("Queue is full.")
        # Add new value to the queue
        self.queue[self.write] = value
        # If write index is at the end of the list, move it to front. Otherwise, move one to right
        self.write = (self.write + 1) % self.size
        
    def dequeue(self):
        # If queue is empty, then raise error
        if self.empty():
            raise Exception("Queue is empty.")
        # Get the output to dequeue
        output = self.queue[self.read]
        # If read index is at the end of the list, move it to front. Otherwise, move one to right
        self.read = (self.read + 1) % self.size
        # Return the dequeued output
        return output
    
    def empty(self):
        return self.read == self.write
    
    def full(self):
        # Check if read index is one after the write index (modulo for circular indexing)
        return (self.write + 1) % self.size == self.read

# For testing, creat an empty queue
q1 = Queue(6)
q1.print_queue()

# Test for empty
print(q1.empty())

# Test for enqueue
q1.enqueue('a')
q1.print_queue()
q1.enqueue('b')
print(q1.empty())
q1.enqueue('c')
q1.print_queue()
q1.enqueue('d')
q1.print_queue()
q1.enqueue('e')
q1.print_queue()
q1.enqueue('f')
q1.print_queue()

# Test for full
print(q1.full())

# Test for dequeue
print(q1.dequeue())
q1.print_queue()
print(q1.dequeue())
q1.print_queue()

# Test for mix
q1.enqueue('g')
q1.print_queue()
print(q1.dequeue())
q1.print_queue()
q1.enqueue('h')
q1.print_queue()
print(q1.dequeue())
q1.print_queue()