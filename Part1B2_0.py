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
