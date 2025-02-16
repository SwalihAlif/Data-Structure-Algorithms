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

    def heapify(self):
        """Converts an unordered array into a valid MaxHeap."""
        for i in range(len(self.heap) // 2, -1, -1):
            self._sink_down(i)
        
    def print_heap(self, index=0, level=0, prefix="Root: "):
        if index >= len(self.heap):  # Fixed condition
            return
        
        right = self._right_child(index)
        if right < len(self.heap):
            self.print_heap(right, level + 1, "R--- ")

        print("   " * level + prefix + str(self.heap[index]))

        left = self._left_child(index)
        if left < len(self.heap):
            self.print_heap(left, level + 1, "L--- ")

# Example usage
myheap = MaxHeap()
myheap.heap = [50, 55, 65, 95, 60, 80, 75]  # Unordered array
print(myheap.heap)
myheap.heapify()  # Converts it into a max heap

print("Heap after heapify:", myheap.heap)
myheap.print_heap()

sorted_array = myheap.heap_sort()
print("Sorted Array:", sorted_array)
