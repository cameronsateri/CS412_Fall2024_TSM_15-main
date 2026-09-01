"""
    name:  Cameron Sateri & Julian Barrett
    assignment: Final Project
    file: tsp_approx
"""
import random


def tsp_greedy(paths, start):
    visited = set()
    current = start
    total_weight = 0.0
    tour = [start]

    while len(visited) < len(paths):
        visited.add(current)
        neighbors = [(neighbor, weight) for neighbor, weight in paths[current].items() if neighbor not in visited]
        if not neighbors:
            break
        # make greedy choice and randomly break ties
        min_weight = min(neighbors, key=lambda x: x[1])[1]
        candidates = [neighbor for neighbor, weight in neighbors if weight == min_weight]
        next_vertex = random.choice(candidates)  # Random tie-breaking
        # update pathing
        total_weight += paths[current][next_vertex]
        tour.append(next_vertex)
        current = next_vertex

    # return to start if possible
    if start in paths[current]:
        total_weight += paths[current][start]
        tour.append(start)
    return total_weight, tour


def main():
    # save n vertices and m edges
    n, m = map(int, input().split())
    # save pathing inputs
    paths = {}
    for _ in range(m):
        u, v, w = input().split()
        w = float(w)
        if u not in paths:
            paths[u] = {}
        paths[u][v] = w
        if v not in paths:
            paths[v] = {}
        paths[v][u] = w
    # run tsp algorithm
    total_weight, tour = tsp_greedy(paths, random.choice(list(paths.keys())))
    # output tsp results
    print(f"{total_weight:.4f}")
    print(" ".join(tour))
    pass


if __name__ == "__main__":
    main()

