from collections import deque


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def is_cyclic(graph, v, visited, parent):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            if is_cyclic(graph, neighbor, visited, v):
                return True
        elif parent != neighbor:
            return True

    return False


def is_bipartite(graph, start):
    color = {}
    queue = deque([start])
    color[start] = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in color:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                return False

    return True


def is_tree(graph):
    visited = {i: False for i in graph}
    

    if is_cyclic(graph, 1, visited, -1):
        return False
    if not all(visited.values()):
        return False
    return True


graph = {
    1: {2, 3},
    2: {1, 4},
    3: {1},
    4: {2}
}


print("DFS:")
dfs(graph, 1)
print("\nBFS:")
bfs(graph, 1)


print("\nChecking for cycle:")
print("Cycle detected:" if is_cyclic(graph, 1, {i: False for i in graph}, -1) else "No cycle detected")

print("\nChecking for bipartiteness:")
print("Graph is bipartite" if is_bipartite(graph, 1) else "Graph is not bipartite")

print("\nChecking if graph is a tree:")
print("Graph is a tree" if is_tree(graph) else "Graph is not a tree")

# This function determines if an undirected graph is a tree. A graph is a tree if it is connected (there's a path between
# every pair of vertices) and contains no cycles. To check for connectivity, we can use either DFS or BFS to start from any
# node and ensure all nodes are reachable. For cycle detection, DFS is employed; the presence of a back-edge indicates a cycle.
# Both DFS and BFS have a running time of O(V + E), where V is the number of vertices and E is the number of edges.
# Therefore, this approach is efficient for both connectivity and cycle checks in a graph.