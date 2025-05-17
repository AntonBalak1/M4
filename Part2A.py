import math

class MinHeap:
    def __init__(self):
        self.heap = []
        self.pos = {}  # Track positions of nodes for decrease_key

    def insert(self, key, val):
        self.heap.append((key, val))
        idx = len(self.heap) - 1
        self.pos[val] = idx
        self._bubble_up(idx)

    def extract_min(self):
        if not self.heap:
            return None
        root = self.heap[0]
        last = self.heap.pop()
        del self.pos[root[1]]
        if self.heap:
            self.heap[0] = last
            self.pos[last[1]] = 0
            self._heapify(0)
        return root

    def decrease_key(self, val, new_key):
        if val not in self.pos:
            return
        i = self.pos[val]
        if self.heap[i][0] <= new_key:
            return
        self.heap[i] = (new_key, val)
        self._bubble_up(i)

    def _bubble_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i][0] < self.heap[parent][0]:
            self.pos[self.heap[i][1]], self.pos[self.heap[parent][1]] = parent, i
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        if left < n and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < n and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right
        if smallest != i:
            self.pos[self.heap[i][1]], self.pos[self.heap[smallest][1]] = smallest, i
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify(smallest)

    def is_empty(self):
        return len(self.heap) == 0

# Dijkstra algorithm
def dijkstra(graph, source):
    dist = {node: math.inf for node in graph}
    dist[source] = 0

    pq = MinHeap()
    for node in graph:
        pq.insert(dist[node], node)

    while not pq.is_empty():
        current_dist, u = pq.extract_min()
        if current_dist == math.inf:
            break
        for neighbor, weight in graph[u]:
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                pq.decrease_key(neighbor, dist[neighbor])

    return dist

# Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    source = 'A'
    shortest_distances = dijkstra(graph, source)
    print("Shortest distances:", shortest_distances)
