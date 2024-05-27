"""
3. Dijkstra's Algorithm (Shortest Path):
Dijkstra's algorithm finds the shortest paths between nodes in a weighted graph.
"""

import heapq


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
weighted_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3, 'G': 7},
    'D': {'B': 2},
    'E': {'B': 5, 'H': 2},
    'F': {'C': 3},
    'G': {'C': 7},
    'H': {'E': 2}
}

start_node = 'A'
shortest_distances = dijkstra(weighted_graph, start_node)
print("\nShortest Distances from {}: {}".format(start_node, shortest_distances))
