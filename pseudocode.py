# path is a list
# cost is total cost
# graph is a list[][]

def verify_certification (path, target_cost, graph):

    # check that the path visits each city once
    # check that first and last city on path are the same
    if len(path) != len(set(path)) or path[0] != path[-1]: 
        return False
    
    # Check that an edge exists for each vertex pair
    total_cost = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        if v not in graph[u]:  # Edge must exist
            return False
        total_cost += graph[u][v]    
    
    return total_cost == target_cost




