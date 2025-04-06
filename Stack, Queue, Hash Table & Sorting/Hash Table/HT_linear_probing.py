class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size  # Directly store (key, value) pairs   
        self.size = size

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % self.size
        return my_hash

    def insert_item(self, key, value):
        index = self.__hash(key)
        original_index = index

        while self.data_map[index] is not None:  # Linear probing
            if self.data_map[index][0] == key:  # Update existing key
                self.data_map[index] = (key, value)
                return
            index = (index + 1) % self.size  # Move to next slot
            if index == original_index:  # Full loop, no space
                raise Exception("HashTable is full")

        self.data_map[index] = (key, value)  # Insert new key-value pair

    def get_item(self, key):
        index = self.__hash(key)
        original_index = index

        while self.data_map[index] is not None:
            if self.data_map[index][0] == key:
                return self.data_map[index][1]
            index = (index + 1) % self.size  # Linear probing
            if index == original_index:  # Full loop
                break
        return None  # Key not found

    def delete_item(self, key):
        index = self.__hash(key)
        original_index = index

        while self.data_map[index] is not None:
            if self.data_map[index][0] == key:
                self.data_map[index] = None  # Mark as deleted (lazy deletion)
                return True
            index = (index + 1) % self.size  # Linear probing
            if index == original_index:
                break
        return False  # Key not found

    def keys(self):
        return [kv[0] for kv in self.data_map if kv is not None]


ht = HashTable(7)

ht.insert_item("apple", 10)
ht.insert_item("banana", 20)
ht.insert_item("grape", 30)

print(ht.get_item("banana"))  # Output: 20
print(ht.get_item("cherry"))  # Output: None

ht.delete_item("banana")
print(ht.get_item("banana"))  # Output: None

ht.print_table()

