# Structure of a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Structure of a linked list
class LinkedList:
    def __init__(self, head = None):
        self.head = head

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

    # Get the size of the list
    def size(self):
        # Starting point
        current = self.head
        s = 0
        # Loop through list until the end
        while current:
            current = current.next
            s += 1
        return s

    # Check if the list is empty
    def empty(self):
        if not self.head:
            return True        
        return False
    
    # Accessing the value at an index
    def value_at(self, index):
        # TODO: implement negative index
        # Check if index is out of bound
        if self.size() < index or index < 0:
            raise Exception("Index out of bound!")
        # Starting point
        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1
        return current.value
    
    def push_front(self, value):
        # Create a new node to add
        new_head = Node(value)
        # If the list is empty then add the new value to list and finish 
        if self.empty():
            self.head = new_head
        else:
            # New head points to the original head
            new_head.next = self.head
            # Update the head of the list to new head
            self.head = new_head
    
    def pop_front(self):
        # If the list is empty then raise Exception 
        if self.empty():
            raise Exception("The list is empty!")
        # Save the value to return
        output = self.head.value
        # Update the head of list
        self.head = self.head.next
        # Return the first item in the list
        return output

    def push_back(self, value):
        # Create a new node to add
        new_tail = Node(value)
        # If the list is empty then add the new value to list and finish 
        if self.empty():
            self.head = new_tail
        else:
            # Get current tail of the list
            current = self.head
            while current.next:
                current = current.next
            # Add the new tail
            current.next = new_tail
    
    def pop_back(self):
        # If the list is empty then raise Exception 
        if self.empty():
            raise Exception("The list is empty!")
        # Get item one before the tail of the list
        current = self.head
        while current.next.next:
            current = current.next
        # Save the value to return
        output = current.next.value
        # Update the tail of the list
        current.next = None
        return output

    def front(self):
        # Get the first item in the list. If list is empty, raise error
        if self.head:
            return self.head.value
        else:
            raise Exception("List is empty.")   

    def back(self):
        # If list is empty, raise error
        if not self.head:
            raise Exception("List is empty.")
        # Go to the tail of the list
        current = self.head
        while current.next:
            current = current.next
        # Return the last item in the list
        return current.value

    def insert(self, index, value):
        # Check if index is valid
        if self.size() < index or index < 0:
            raise Exception("Index is out of bound!")
        # Create a new node to add
        new_node = Node(value)
        # Go to one before the index in the list
        current = self.head
        i = 0
        while i < index - 1:
            current = current.next
            i += 1
        # New node points to the item that is currently at the index
        new_node.next = current.next
        # Connect the item one before the index to new node
        current.next = new_node

    def erase(self, index):
        # Check if index is valid
        if self.size() < index or index < 0:
            raise Exception("Index is out of bound!")
        # Go to one before the index in the list
        current = self.head
        i = 0
        while i < index - 1:
            current = current.next
            i += 1
        # Connect the item one before the index to the item one after the index
        current.next = current.next.next
    
    def value_n_from_end(self, n):
        # Get the target index
        index = self.size() - n
        # Check if index is valid
        if index < 0:
            raise Exception("The input value is not valid.")
        # Go to the index in the list
        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1
        # Return the value at the index
        return current.value
    
    def reverse(self):
        # Create a new head
        new_head = None
        # Loop through the list
        while self.head:
            # Move the head and change the direction of the head. The new head becomes the previous item in the list
            self.head.next, self.head, new_head = new_head, self.head.next, self.head
        # Define the new head
        self.head = new_head

    def remove_value(self, value):
        # If the first item has the equal value, then simply change the head of list to the second item in the list
        if self.head.value == value:
            self.head = self.head.next
        else:
            # Starting point (we know that head is not equal to the input value due to if statement)
            current = self.head
            # Loop through the items in the list
            while current.next:
                # If the equal value is found simply connect the one before to one after
                if current.next.value == value:
                    current.next = current.next.next
                    break
                current = current.next
            # TODO: flag when the value is not found in the list


# For test, initialize nodes with values corresponding the digits of pi
n1 = Node(3)
n2 = Node(1)
n3 = Node(4)
n4 = Node(1)
n5 = Node(5)

# Link the nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Test for getting the size of the list
l1 = LinkedList(n1)
print("Size of l1: {}".format(l1.size()))

# Test for checking empty list
l2 = LinkedList()
print("Is l2 empty? {}".format(l2.empty()))
# If head node is initialized, the list is no longer empty
l2.head = n4
print("Is l2 empty? {}".format(l2.empty()))
print("Size of l2: {}".format(l2.size()))

# Test for accessing value at an index
print("The value at index 2 of l1 is {}".format(l1.value_at(2)))
l1.print_list("l1")
# print(l2.value_at(3))
# print(l1.value_at(-1))

# Test for push front
l1.push_front(1)
l1.print_list("l1")
l3 = LinkedList()
l3.push_front(3)
l3.print_list("l3")

# Test for pop front
print("The first item in list l1 is: {}".format(l1.pop_front()))
l1.print_list("l1")
# l4 = LinkedList()
# print(l4.pop_front())

# Test for push back
l1.push_back(9)
l1.print_list("l1")
l5 = LinkedList()
l5.push_back(3)
l5.print_list("l5")

# Test for pop back
print("The last item in list l1 is: {}".format(l1.pop_back()))
l1.print_list("l1")
# l6 = LinkedList()
# print(l6.pop_back())

# Test for front
print("The first item in the list l1 is {}".format(l1.front()))

# Test for front
print("The last item in the list l1 is {}".format(l1.back()))

# Test for insert
l1.print_list("l1")
l1.insert(2, 9)
l1.print_list("l1")
l1.insert(4, 7)
l1.print_list("l1")

# Test for erase
l1.erase(2)
l1.print_list("l1")
l1.erase(3)
l1.print_list("l1")

# Test for value n from end
print("The 1st value from the end of list l1 is {}".format(l1.value_n_from_end(1)))
print("The 3rd value from the end of list l1 is {}".format(l1.value_n_from_end(3)))
# print("The 6th value from the end of list l1 is {}".format(l1.value_n_from_end(6)))

# Test for reverse
l1.print_list("l1")
l1.reverse()
l1.print_list("l1")

# Test for remove value
l1.remove_value(1)
l1.print_list("l1")
l1.remove_value(6)
l1.print_list("l1")
l1.remove_value(1)
l1.print_list("l1")