class HashTable:
    def __init__(self, size = 7):
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
            

my_hash_table = HashTable()
my_hash_table.print_table()
print('-------------------------------')
my_hash_table.insert_item('mango', 45)
my_hash_table.insert_item('apple', 450)
my_hash_table.insert_item('pine apple', 145)
my_hash_table.print_table()
print('-------------------------------')
print('pine apple: ', my_hash_table.get_item('pine apple'))