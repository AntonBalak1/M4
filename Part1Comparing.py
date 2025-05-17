import time
import random
import random

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify(0)
        return root

    def decrease_key(self, i, new_key):
        if i < 0 or i >= len(self.heap) or new_key > self.heap[i]:
            return  # Invalid index or key not smaller
        self.heap[i] = new_key
        self._bubble_up(i)

    def _bubble_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify(smallest)

    def __str__(self):
        return str(self.heap)




random_list = random.sample(range(1, 100), 10)
print("Random Input:", random_list)

# Initialize and test MinHeap
heap = MinHeap()
for num in random_list:
    heap.insert(num)

print("Heap after inserts:", heap)

# Extract min
min_val = heap.extract_min()
print("Extracted Min:", min_val)
print("Heap after extraction:", heap)

# Decrease a key
index_to_decrease = 5
new_value = heap.heap[index_to_decrease] - 5
heap.decrease_key(index_to_decrease, new_value)
print(f"Heap after decreasing key at index {index_to_decrease} to {new_value}:", heap)

class TernaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return root

    def _bubble_up(self, i):
        parent = (i - 1) // 3
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 3

    def _heapify(self, i):
        smallest = i
        children = [3*i + j for j in range(1, 4)]
        for child in children:
            if child < len(self.heap) and self.heap[child] < self.heap[smallest]:
                smallest = child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify(smallest)

class DaryHeap:
    def __init__(self, d=2):
        if d < 2:
            raise ValueError("Branching factor d must be >= 2")
        self.d = d
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return root

    def _bubble_up(self, i):
        parent = (i - 1) // self.d
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // self.d

    def _heapify(self, i):
        smallest = i
        children = [self.d * i + j for j in range(1, self.d + 1)]
        for child in children:
            if child < len(self.heap) and self.heap[child] < self.heap[smallest]:
                smallest = child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify(smallest)


def test_heap_performance(heap_class, d, n=100000):
    heap = heap_class(d) if d else heap_class()  # d is None for binary/ternary classes
    data = random.sample(range(n * 10), n)

    start = time.time()
    for x in data:
        heap.insert(x)
    insert_time = time.time() - start

    start = time.time()
    while True:
        val = heap.extract_min()
        if val is None:
            break
    extract_time = time.time() - start

    return insert_time, extract_time

if __name__ == "__main__":
    n = 100000

    print("Binary Heap:")
    ins, ext = test_heap_performance(MinHeap, None, n)
    print(f"Insert: {ins:.3f}s, Extract: {ext:.3f}s")

    print("Ternary Heap:")
    ins, ext = test_heap_performance(TernaryHeap, None, n)
    print(f"Insert: {ins:.3f}s, Extract: {ext:.3f}s")

    print("d-ary Heap (d=4):")
    ins, ext = test_heap_performance(DaryHeap, 4, n)
    print(f"Insert: {ins:.3f}s, Extract: {ext:.3f}s")

    print("d-ary Heap (d=8):")
    ins, ext = test_heap_performance(DaryHeap, 8, n)
    print(f"Insert: {ins:.3f}s, Extract: {ext:.3f}s")
