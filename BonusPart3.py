import matplotlib.pyplot as plt

def plot_tsp_path(coords, path):
    xs, ys = zip(*[coords[i] for i in path])
    plt.figure(figsize=(8,6))
    plt.plot(xs, ys, 'o-')
    for i, (x, y) in enumerate(coords):
        plt.text(x, y, f'{i}', fontsize=12)
    plt.title("TSP Path")
    plt.show()

coords = [(0,0), (1,5), (5,2), (6,6)]  # example city coordinates
plot_tsp_path(coords, path)
