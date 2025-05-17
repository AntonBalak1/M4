def tsp_nearest_neighbor(dist_matrix):
    n = len(dist_matrix)
    visited = [False] * n
    path = [0]
    visited[0] = True
    total_cost = 0
    current = 0

    for _ in range(n - 1):
        next_city = None
        min_dist = float('inf')
        for city in range(n):
            if not visited[city] and dist_matrix[current][city] < min_dist:
                min_dist = dist_matrix[current][city]
                next_city = city
        path.append(next_city)
        visited[next_city] = True
        total_cost += min_dist
        current = next_city

    # Return to start city
    total_cost += dist_matrix[current][0]
    path.append(0)
    return path, total_cost

path, cost = tsp_nearest_neighbor(dist_matrix)
print("Nearest Neighbor TSP Path:", path)
print("Cost:", cost)
