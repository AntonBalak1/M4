from fibonacci_heap_mod import Fibonacci_heap

def dijkstra_fibonacci(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    fib_heap = Fibonacci_heap()
    nodes = {}

    # Insert nodes with keys (distances)
    for node in graph:
        nodes[node] = fib_heap.enqueue(node, dist[node])  # enqueue(value, key)

    while fib_heap.total_nodes > 0:
        min_node = fib_heap.dequeue_min()  # dequeue_min() returns the node with smallest key
        u = min_node.value
        for neighbor, weight in graph[u]:
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                fib_heap.decrease_key(nodes[neighbor], dist[neighbor])

    return dist

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    source = 'A'
    shortest_distances = dijkstra_fibonacci(graph, source)
    print("Shortest distances:", shortest_distances)

