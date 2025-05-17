import heapq

def tsp_branch_and_bound(dist_matrix):
    n = len(dist_matrix)
    # Priority queue stores tuples: (estimated_cost, path, cost_so_far, visited_set)
    pq = []
    start = 0
    initial_path = [start]
    visited = set([start])
    initial_cost = 0

    # Heuristic: simple lower bound — sum of min edges from unvisited nodes
    def heuristic(visited):
        unvisited = set(range(n)) - visited
        if not unvisited:
            return 0
        # sum of min outgoing edges for each unvisited node
        return sum(min(dist_matrix[u][v] for v in range(n) if v != u) for u in unvisited)

    heapq.heappush(pq, (initial_cost + heuristic(visited), initial_path, initial_cost, visited))

    best_cost = float('inf')
    best_path = None

    while pq:
        est_cost, path, cost_so_far, visited = heapq.heappop(pq)

        if est_cost >= best_cost:
            continue  # prune

        if len(path) == n:
            # complete path, add cost to return to start
            total_cost = cost_so_far + dist_matrix[path[-1]][start]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path + [start]
            continue

        current = path[-1]
        for next_city in range(n):
            if next_city not in visited:
                new_cost = cost_so_far + dist_matrix[current][next_city]
                new_visited = visited | {next_city}
                est = new_cost + heuristic(new_visited)
                if est < best_cost:
                    heapq.heappush(pq, (est, path + [next_city], new_cost, new_visited))

    return best_path, best_cost

path, cost = tsp_branch_and_bound(dist_matrix)
print("Heap-Based TSP Path:", path)
print("Cost:", cost)
