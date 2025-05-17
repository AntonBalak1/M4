import itertools

def tsp_brute_force(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(n))
    min_cost = float('inf')
    best_path = None

    for perm in itertools.permutations(cities[1:]):  # Fix start city as 0
        path = [0] + list(perm) + [0]
        cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

# Example usage:
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = tsp_brute_force(dist_matrix)
print("Brute Force TSP Path:", path)
print("Cost:", cost)
