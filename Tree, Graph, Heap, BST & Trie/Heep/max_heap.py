class MaxHeap:
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
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

    def heap_sort(self):
        sorted_array = []
        while self.heap:
            sorted_array.append(self.remove())
        return sorted_array[::-1]  # Reverse to get ascending order
    
    def print(self):
        def print_heap(heap, index=0, level=0, prefix="Root: "):
            if index >= len(heap):
                return
            
            right = 2 * index + 2
            left = 2 * index + 1
            
            if right < len(heap):
                print_heap(heap, right, level + 1, "R---")
            print("  " * level + prefix + str(heap[index]))
            if left < len(heap):
                print_heap(heap, left, level + 1, 'L---')
                
        print_heap(self.heap)

myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)

myheap.remove()
print(myheap.heap)

myheap.remove()
print(myheap.heap)

myheap.print()
sorted_array = myheap.heap_sort()
print("Sorted Array:", sorted_array)
