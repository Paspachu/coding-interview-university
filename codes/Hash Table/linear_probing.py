# Hash table with linear probing
class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
    
    def print_ht(self):
        # If the table is empty, then raise an error
        if self.empty():
            raise Exception("Empty table.")
        # Loop through the array and print only the existing items
        for key, value in zip(self.keys, self.values):
            if key:
                print("{} = {}".format(key, value))

    def empty(self):
        for key in self.keys:
            if key:
                return False
        return True

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        
        while self.keys[index]:
            # If the key already exists, update the value and return
            if self.keys[index] == key:
                self.values[index] = value
                return
            # Otherwise, we implement linear probing
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value


    

# Initialization for testing
ht1 = HashTable(10)
print(ht1.empty())

# Add items
ht1.add('apple', 'really bad')
ht1.add(3, 5)
ht1.print_ht()
print(ht1.empty())



