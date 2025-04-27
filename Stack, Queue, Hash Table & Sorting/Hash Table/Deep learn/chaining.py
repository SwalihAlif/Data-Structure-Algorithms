class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def print_table(self):
        for i, val in enumerate(self.table):
            print(i, ':', val)

    def get_hash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size
    
    def __setitem__(self, key, value):
        index = self.get_hash(key)
        if self.table[index] == None:
            self.table[index] = []
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def __getitem__(self, key):
        index = self.get_hash(key)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        raise KeyError(f"Key {key} is not found.")
    
    def __delitem__(self, key):
        index = self.get_hash(key)
        if self.table[index] is not None:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    if len(self.table[index]) == 0:
                        self.table[index] = None
                    return

        raise KeyError(f"key {key} is not found.")

t = HashTable()
t.__setitem__('march 6', 45)
t.__setitem__('march 12', 457)
t.__setitem__('march 14', 435)
t.__setitem__('march 5', 145)
t.__setitem__('march 17', 450)
t.__setitem__('march 19', 500)
t.__setitem__('march 6', 455)
t.print_table()
print(t.__getitem__('march 6'))
t.__delitem__('march 19')
t.print_table()
