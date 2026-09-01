from itertools import permutations

def parse_input():
    n, m = map(int, input().split())

    graph = {}
    vertices = []
    for _ in range(m):
        u, v, w = input().split()
        w = float(w)
        if u not in graph:
            graph[u] = {}
            vertices.append(u)
        if v not in graph:
            graph[v] = {}
            vertices.append(v)
        graph[u][v] = w
        graph[v][u] = w

    return vertices, graph

def tsp_brute_force(vertices, graph):
    start = vertices[0]  # Start from the first vertex
    shortest_path = None
    min_length = float('inf')

    # Generate all permutations of the other vertices excluding the start vertex
    for perm in permutations(vertices[1:]): # (n-1)! permutations
        cycle = [start] + list(perm) + [start]
        length = 0
        for i in range(len(cycle) - 1): # calculate cost of cycle
            u, v = cycle[i], cycle[i + 1]
            length += graph[u][v]

        # Check if this cycle is the shortest
        if length < min_length:
            min_length = length
            shortest_path = cycle

    return min_length, shortest_path

def main():
    vertices, graph = parse_input()
    min_length, shortest_path = tsp_brute_force(vertices, graph)
    print(f"{min_length:.4f}")
    print(' '.join(shortest_path))

if __name__ == "__main__":
    main()
