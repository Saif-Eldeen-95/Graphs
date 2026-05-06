from collections import deque, defaultdict


# ── 1. BFS-based Topological Sort ──────────────────────────────────────────
def topological_sort_bfs(graph, vertices):
    """
    Kahn's Algorithm using in-degree tracking + BFS queue.
    Detects cycles: returns None if graph is not a DAG.
    """
    in_degree = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Start with all nodes that have no incoming edges (in-degree = 0)
    queue = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(vertices):
        return None  # Cycle detected → not a DAG

    return topo_order


# ── 2. DFS-based Topological Sort ────────────────────────────────────────────
def topological_sort_dfs(graph, vertices):
    """
    DFS-based approach using a visited set and an explicit stack result.
    A node is pushed to the result AFTER all its descendants are processed.
    """
    visited = set()
    result_stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        result_stack.append(node)  # push after all descendants

    for v in vertices:
        if v not in visited:
            dfs(v)

    return result_stack[::-1]  # reverse → correct topo order
# ── example usage ──────────────────────────────────────────────────────
graph = {
    5: [0, 2],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: [],
}
vertices = [0, 1, 2, 3, 4, 5]

bfs_result = topological_sort_bfs(graph, vertices)
dfs_result  = topological_sort_dfs(graph, vertices)

print("BFS-based:   ", bfs_result)
print("DFS-based:   ", dfs_result)


# ── Cycle detection demo ──────────────────────────────────────────────────────
cyclic_graph = {
    0: [1],
    1: [2],
    2: [0],  # cycle!
}
print("\nCycle detected (BFS):", topological_sort_bfs(cyclic_graph, [0, 1, 2]))