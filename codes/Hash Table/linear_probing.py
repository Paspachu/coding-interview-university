# Hash table with linear probing
class HashTable:
    def __init__(self, size):
        self.count = 0
        self.size = size
        # There are two arrays here. Not sure if using one array with tuple is better, or if there is other better way
        self.keys = [None] * self.size
        self.values = [None] * self.size
    
    def print_ht(self):
        # If the table is empty, then raise an error
        if self.empty():
            raise Exception("Empty table.")
        
        # Choice 1: Print in tuple to print out entire table, including the null values
        print(tuple(zip(self.keys, self.values)))
        # Choice 2: Loop through the array and print only the existing items
        # for key, value in zip(self.keys, self.values):
        #     if key:
        #         print("{} = {}".format(key, value))

    def empty(self):
        # Check if any one key is not null.
        for key in self.keys:
            if key:
                return False
        return True

    def hash_function(self, key, N):
        # The hash function in Python changes every run
        return hash(key) % N

    def doubling_table(self):
        # Initialize a new hash table
        new_size = self.size * 2
        new_keys = [None] * new_size
        new_values = [None] * new_size
        
        # Loop through the old table and add each item to the new table
        for old_index in range(self.size):
            if self.keys[old_index]:
                new_index = self.hash_function(self.keys[old_index], new_size)
                # For collision, use linear probing
                while new_keys[new_index]:
                    new_index = (new_index + 1) % new_size
                # Add the item to the new arrays
                new_keys[new_index] = self.keys[old_index]
                new_values[new_index] = self.values[old_index]
        
        # Update the table with the new keys and values
        self.size = new_size
        self.keys = new_keys
        self.values = new_values

    def add(self, key, value):
        index = self.hash_function(key, self.size)
        
        while self.keys[index]:
            # If the key already exists, update the value and return
            if self.keys[index] == key:
                self.values[index] = value
                return
            # Otherwise, we implement linear probing
            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value
        self.count += 1

        if self.count > self.size // 2:
            self.doubling_table()

    def exists(self, key):
        # This is good thing about the hash table. Simply get the index from the hash function and return if the key exists or not
        index = self.hash_function(key, self.size)
        # Check if the key exists
        while self.keys[index]:
            # If the key is there, then return True
            if self.keys[index] == key:
                return True
            # Otherwise, performing linear probing
            index = (index + 1) % self.size
        # If the key does not exists, then return False
        return False
        
    def get(self, key):
        # First check if the key exists.
        if not self.exists(key):
            raise Exception("The key does not exists.")
        # Get index from the hash function and return the value at that index
        index = self.hash_function(key, self.size)
        # Perform linear probing, until we get the correct key match
        while self.keys[index] != key:
            index = (index + 1) % self.size
        # Then, we return the value for the corresponding key
        return self.values[index]
    
    def remove(self, key):
        # First check if the key exists
        if not self.exists(key):
            raise Exception("The key does not exists.")
        # Get index from the hash function
        index = self.hash_function(key, self.size)
        # Perform linear probing, until we get the correct key match
        while self.keys[index] != key:
            index = (index + 1) % self.size
        # Then, we remove the item
        self.keys[index] = None
        self.values[index] = None

# Initialization for testing
ht1 = HashTable(5)
print(ht1.empty())

# Add items
ht1.add('apple', 'really bad')
ht1.print_ht()
ht1.add(3, 5)
ht1.print_ht()
ht1.add('cucumber', 'like')
ht1.print_ht()
print(ht1.empty())

# Add more items and test updating also
ht1.add('cucumber', 'really good')
ht1.print_ht()
ht1.add(99, 101)
ht1.print_ht()
ht1.add('fried food', 'really bad')
ht1.print_ht()
ht1.add(101, 51)
ht1.print_ht()

# Test for exists
print(ht1.exists('apple'))
print(ht1.exists(5))

# Test for get
print(ht1.get('cucumber'))
print(ht1.get(101))
# print(ht1.get(7))

# Test for remove
ht1.remove(101)
ht1.print_ht()
ht1.remove('apple')
ht1.print_ht()
# ht1.remove(5)
# ht1.print_ht()


