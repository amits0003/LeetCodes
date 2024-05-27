"""
2. Depth-First Search (DFS):
DFS explores as far as possible along each branch before backtracking.
It is often used for topological sorting, connected components, and detecting cycles.
"""
from GraphAlgo_Breadth_First_Search import graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)


# Example usage:
print("\nDFS Traversal:")
dfs(graph, 'A')
