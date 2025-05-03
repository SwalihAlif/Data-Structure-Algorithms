class HashTable:
    def __init__(self, size = 10):
        self.data_map = [None] * size
        
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)
            
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 17) % len(self.data_map)
        return my_hash
        
    def insert_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] != None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                    
        return None
    
    def __delitem__(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    del self.data_map[index][i]
                    print(f"The key {key} is deleted")
                    return
        print(f"The key {key} is not found..")
            

my_hash_table = HashTable()
my_hash_table.print_table()
print('-------------------------------')
my_hash_table.insert_item('march 6', 45)
my_hash_table.insert_item('march 17', 450)
my_hash_table.insert_item('pine apple', 145)
my_hash_table.print_table()
print('-------------------------------')
print('pine apple: ', my_hash_table.get_item('pine apple'))
my_hash_table.__delitem__('march 6') 