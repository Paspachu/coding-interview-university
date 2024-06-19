class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def print_queue(self):
        if self.empty():
            print("")
            return
        current = self.head
        print_line = ""
        while current:
            print_line += "{}, ".format(current.value)
            current = current.next
        print(print_line[:-2])
    
    def enqueue(self, value):
        # Create a node to add to queue
        new_node = Node(value)
        # If the list is empty, connect head and tail to new_node. Otherwise, current tail points to new node and new node becomes the tail
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        # If the queue is empty, raise an error
        if self.empty():
            raise Exception("Empty queue.")
        # Get the ouput value
        output = self.head.value
        # Update the head to the next item in the queue
        self.head = self.head.next
        # If the queue is empty after dequeue, then update tail to point None
        if not self.head:
            self.tail = None
        # Return the dequeued item
        return output

    def empty(self):
        # If the head points to None, the queue is empty
        return not self.head
    
# For testing, creat an empty queue
q1 = Queue()
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

# Test for dequeue
print(q1.dequeue())
q1.print_queue()
print(q1.dequeue())
q1.print_queue()

# Test for mix
q1.enqueue('e')
q1.print_queue()
print(q1.dequeue())
q1.print_queue()
q1.enqueue('f')
q1.print_queue()
print(q1.dequeue())
q1.print_queue()
    
