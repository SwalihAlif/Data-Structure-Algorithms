class MinHeap:
    def __init__(self):
        self.heap = []
        
    def _left_child(self, index):
        return 2 * index + 1
        
    def _right_child(self, index):
        return 2 * index + 2
        
    def _parent(self, index):
        return (index - 1) // 2
        
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current:
            if current > 0 and self.heap[current] < self.heap[self._parent(current)]:
                self._swap(current, self._parent(current))
                current = self._parent(current)
                
my_heap = MinHeap()
my_heap.insert(1)
my_heap.insert(2)
my_heap.insert(3)
my_heap.insert(4)
my_heap.insert(5)
print(my_heap.heap)