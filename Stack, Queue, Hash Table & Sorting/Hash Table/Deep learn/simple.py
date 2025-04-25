class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def get_hash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size
    
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        self.table[index] = value

    def __getitem__(self, key):
        index = self.get_hash(key)
        value = self.table[index]
        if value is None:
            raise KeyError(f"Key '{key}' not found.")
        return value
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        if self.table[index] is None:
            raise KeyError(f"Key '{key}' not found.")
        self.table[index] = None

    def print_table(self):
        for i, val in enumerate(self.table):
            print(i, ':', val)

t = HashTable()
t.__setitem__('march 6', 45)
t.__setitem__('march 17', 450)
t.print_table()
print("Value at 'march 6': ", t.__getitem__('march 6'))

t.__delitem__('march 6')
print("\nAfter deleting 'march 6': ")
t.print_table()

# By using python's __exmple__ methods we can insert values like we are 
# doing with dictionaries

# t = HashTable()
# t['march 6'] = 45
# t['march 17'] = 450

# t.print_table()
# print("Value at 'march 6':", t['march 6'])

# del t['march 6']
# print("\nAfter deleting 'march 6':")
# t.print_table()