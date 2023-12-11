import sys

def nearest_neighbor_tsp(graph, start_node):
    visited = [start_node]
    total_distance = 0

    while len(visited) < len(graph):
        current_node = visited[-1]
        nearest_node = None
        min_distance = sys.maxsize

        for node, distance in graph[current_node].items():
            if node not in visited and distance < min_distance:
                nearest_node = node
                min_distance = distance

        if nearest_node is None:
            break

        visited.append(nearest_node)
        total_distance += min_distance

    if visited[-1] in graph[start_node]:
        total_distance += graph[visited[-1]][start_node]
        visited.append(start_node)

    return visited, total_distance

graph = {
    'A': {'B': 2, 'C': 3, 'D': 1,'F':2},
    'B': {'A': 2, 'C': 4, 'E': 5},
    'C': {'A': 3, 'B': 4, 'D': 2},
    'D': {'A': 1, 'C': 2, 'F': 4},
    'E': {'B': 5, 'F': 3},
    'F': {'D': 4, 'E': 3,'A':2}
}

start_node = 'A'

shortest_path, shortest_distance = nearest_neighbor_tsp(graph, start_node)
print("Shortest TSP path:", shortest_path)
print("Shortest TSP distance:", shortest_distance)