# Node class for doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Doubly Linked List class with head and tail
class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_list(self, listname):
        # Starting point
        current = self.head
        output = "The list " + listname + " looks like: "
        # Loop through the list until the end
        while current:
            output += str(current.value) + ", "
            current = current.next
        # Print the list excluding the last two elements in the string, which are ", "
        print(output[:-2])

    def size(self):
        # Start from the head of the list
        current = self.head
        s = 0
        # Loop through the list until we reach the tail of the list
        while current:
            current = current.next
            s += 1
        return s
    
    def empty(self):
        # Check the size of the list and if 0 return True else return False
        if self.size() == 0:
            return True
        return False
    
    def value_at(self, index):
        # Get the size of the list
        n = self.size()
        # Check if the index is out of bound
        if index >= n or index < 0:
            raise Exception("Index is out of bound")
        # If index is in first half then start from head, otherwise start from tail
        if index <= n // 2:
            current = self.head
            i = 0
            while i < index:
                current = current.next
                i += 1
        else:
            current = self.tail
            i = n - 1
            while i > index:
                current = current.prev
                i -= 1
        return current.value
    
    def push_front(self, value):
        # Create a new node to add
        new_head = Node(value)
        # If the list is empty, add the new node to head and tail
        if self.empty():
            self.head = new_head
            self.tail = new_head
        else: 
            # Connect new head to current head
            new_head.next = self.head
            self.head.prev = new_head
            # Renew the head of the list to new head
            self.head = new_head
    
    def pop_front(self):
        # If the list is empty then raise Exception 
        if self.empty():
            raise Exception("The list is empty!")
        # Save the output to pop
        output = self.head.value
        # Simply renew the head of list to one next node to the current head
        new_head = self.head.next
        self.head = new_head
        # If the new head is present, then change the prev pointer to point None. Otherwise, both head and tail point None
        if new_head:
            new_head.prev = None
        else:
            self.head = None
            self.tail = None
        return output
    
    def push_back(self, value):
        # Create a new node to add
        new_tail = Node(value)
        # If the list is empty, add the new node to head and tail
        if self.empty():
            self.head = new_tail
            self.tail = new_tail
        else: 
            # Connect new tail to current tail
            self.tail.next = new_tail
            new_tail.prev = self.tail
            # Renew the tail of the list to new tail
            self.tail = new_tail
    
    def pop_back(self):
        # If the list is empty then raise Exception 
        if self.empty():
            raise Exception("The list is empty!")
        # Save the output to pop
        output = self.tail.value
        # Simply renew the tail of list to one previous node to the current tail
        new_tail = self.tail.prev
        self.tail = new_tail
        # If the new tail is present, then change the next pointer to point None. Otherwise, both head and tail point None
        if new_tail:
            new_tail.next = None
        else:
            self.head = None
            self.tail = None
        return output

    def front(self):
        if self.head:
            return self.head.value
        else:
            raise Exception("List is empty.")

    def back(self):
        if self.tail:
            return self.tail.value
        else:
            raise Exception("List is empty.")

    def insert(self, index, value):
        # Get the size of the list
        n = self.size()
        # Check if the index is out of bound
        if index >= n or index < 0:
            raise Exception("Index is out of bound")
        # If index is the start, call the push front function
        if index == 0:
            self.push_front(value)
            return
        # If the index is the end, call the push back function
        if index == n - 1:
            self.push_back(value)
            return
        
        # If index is in first half then start from head, otherwise start from tail
        if index <= n // 2:
            current = self.head
            i = 0
            while i < index:
                current = current.next
                i += 1
        else:
            current = self.tail
            i = n - 1
            while i > index:
                current = current.prev
                i -= 1
        
        # Initialize the previous and next node
        prev_node = current.prev
        next_node = current
        # Create a new node to add
        new_node = Node(value)
        # Connect the new node to previous node and next node
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def erase(self, index):
        # Get the size of the list
        n = self.size()
        # Check if the index is out of bound
        if index >= n or index < 0:
            raise Exception("Index is out of bound")
        # If index is the start, call the pop front function
        if index == 0:
            self.pop_front()
            return
        # If the index is the end, call the pop back function
        if index == n - 1:
            self.pop_back()
            return
        
        # If index is in first half then start from head, otherwise start from tail
        if index <= n // 2:
            current = self.head
            i = 0
            while i < index:
                current = current.next
                i += 1
        else:
            current = self.tail
            i = n - 1
            while i > index:
                current = current.prev
                i -= 1

        # Initialize the previous and next node
        prev_node = current.prev
        next_node = current.next
        # Connect previous node and next node
        prev_node.next = next_node
        next_node.prev = prev_node

    def value_n_from_end(self, n):
        # Check if list is empty
        if self.empty():
            raise Exception("The list is empty.")
        # Check if n is valid
        if n > self.size():
            raise Exception("Input n is not a valid value.")
        # Start from tail and go backwards until n
        current = self.tail
        i = 1
        while i < n:
            current = current.prev
            i += 1
        return current.value

    def reverse(self):
        # Go through the list and change the direction of the pointer
        current = self.head
        while current:
            temp = current.next
            current.next, current.prev = current.prev, current.next
            current = temp
        # Then, we simply swap the head and tail
        self.head, self.tail = self.tail, self.head

    def remove_value(self, value):
        # Go through the list and find the first appearance of the value
        current = self.head
        while current:
            if current.value == value:
                # Handle the endpoints
                if current == self.head:
                    self.pop_front()
                elif current == self.tail:
                    self.pop_back()
                else:
                    # Remove the value
                    prev_node = current.prev
                    next_node = current.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                break
            current = current.next

def main():
    # For test, initialize nodes with values corresponding the digits of pi
    n1 = Node(3)
    n2 = Node(1)
    n3 = Node(4)
    n4 = Node(1)
    n5 = Node(5)

    # Link the nodes
    n1.next = n2
    n2.prev = n1
    n2.next = n3
    n3.prev = n2
    n3.next = n4
    n4.prev = n3
    n4.next = n5
    n5.prev = n4

    # Create sample doubly linked list
    l1 = DoublyLL()
    l1.head = n1
    l1.tail = n5

    # Print the entire list and the size of the list
    l1.print_list("l1")
    print("The size of l1 is: {}".format(l1.size()))

    # Check if the list is empty
    print("Is l1 empty?: {}".format(l1.empty()))
    l2 = DoublyLL()
    print("Is l2 empty?: {}".format(l2.empty()))

    # Test for value at an index
    print("The value at index 2 in l1 is: {}".format(l1.value_at(2)))
    print("The value at index 4 in l1 is: {}".format(l1.value_at(4)))

    # Test for push front
    l1.push_front(1)
    l1.print_list("l1")
    l2.push_front(9)
    l2.push_front(8)
    l2.print_list("l2")

    # Test for pop front
    print("The first item poped is: {}".format(l1.pop_front()))
    l1.print_list("l1")
    print("The first item poped is: {}".format(l2.pop_front()))
    l2.print_list("l2")
    print("The first item poped is: {}".format(l2.pop_front()))
    l2.print_list("l2")

    # Test for push back
    l1.push_back(9)
    l1.print_list("l1")
    l2.push_back(9)
    l2.push_back(8)
    l2.print_list("l2")

    # Test for pop back
    print("The last item poped is: {}".format(l1.pop_back()))
    l1.print_list("l1")
    print("The last item poped is: {}".format(l2.pop_back()))
    l2.print_list("l2")
    print("The last item poped is: {}".format(l2.pop_back()))
    l2.print_list("l2")

    # Test for front and back
    print("The first item in l1 is: {}".format(l1.front()))
    print("The last item in l1 is: {}".format(l1.back()))
    # print("The first item in l2 is: {}".format(l2.front()))
    # print("The last item in l2 is: {}".format(l2.back()))

    # Test for insert
    l1.insert(2, 9)
    l1.print_list("l1")

    # Test for erase
    l1.erase(2)
    l1.print_list("l1")

    # Test for value n from end
    print("The 3rd value from the end of list l1 is: {}".format(l1.value_n_from_end(3)))

    # Test for reverse
    l1.print_list("l1")
    l1.reverse()
    l1.print_list("l1")
    l1.reverse()
    l1.print_list("l1")

    # Test for remove_value
    l1.remove_value(1)
    l1.print_list("l1")

if __name__ == '__main__':
    main()